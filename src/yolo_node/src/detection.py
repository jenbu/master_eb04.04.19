
from PIL import Image as PILImage

import rospy
import ros
import time
import numpy as np
from timeit import default_timer as timer
from sensor_msgs.msg import Image, CameraInfo
import message_filters
from yolo_node.msg import detection_info
import cv2
import argparse
from keras_yolo3.yolo import YOLO
import tensorflow as tf


import sys
from cv_bridge import CvBridge, CvBridgeError
#sys.path.insert(0, '/home/erlendb/Programmering/PCL/kinect_ws/src/kinectTesting/src/keras-yolo3')
#print(sys.path)
#from kinectTesting.src.yolo_video import detect_img


class Receiver(object):#I python 2 burde man skrive klassen som dette her, det gir flere fordeler som @classmethods, @staticmethods og mer. i Python3 trenger man ikke aa skrive den slik etter som det er standard
    def __init__(self, args):
        self.colorImage = None
        self.img = None
        self.pilImg = None
        self.yolo = YOLO(**vars(args))
        self.publishers = []
        self.callback_list = []



        self.detection_info_msg = detection_info()
        self.pub_detection = rospy.Publisher("/detection_info_publisher", detection_info)
        self.pub_color_image = rospy.Publisher("/detection_color", Image)
        self.pub_color_info = rospy.Publisher("/detection_color_info", CameraInfo)
        self.pub_depth_image = rospy.Publisher("/detection_depth", Image)
        self.pub_depth_info = rospy.Publisher("/detection_depth_info", CameraInfo)
        #self.publishers[0] = rospy.Publisher("/detection_info_publisher", detection_info)
        #self.publishers[1] = rospy.Publisher("/detection_color", Image)
        #self.publishers[2] = rospy.Publisher("/detection_color_info", CameraInfo)
        #self.publishers[3] = rospy.Publisher("/detection_depth", Image)
        #self.publishers[4] = rospy.Publisher("/detection_depth_info", CameraInfo)


        self.bridge = CvBridge()
        #self.image_sub = rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, self.callback)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video = cv2.VideoWriter("/home/erlendb/Programmering/PCL/kinect_ws/test.avi", self.fourcc, 30, (960, 540))

        self.running = None

        #FPS variables
        self.accum_time = 0
        self.curr_fps = 0
        self.prev_time = timer()
        self.fps = "FPS: ??"


    def start(self):
        print("Start()")

        #Subscribers, using TimeSynchronization
        image_color_sub = message_filters.Subscriber('/kinect2/qhd/image_color_rect', Image)
        image_info_sub = message_filters.Subscriber('/kinect2/qhd/camera_info', CameraInfo)
        image_depth_sub = message_filters.Subscriber('/kinect2/qhd/image_depth_rect', Image)
        image_depth_info_sub = message_filters.Subscriber('/kinect2/qhd/camera_info', CameraInfo)

        ts = message_filters.TimeSynchronizer([image_color_sub, image_info_sub, image_depth_sub, image_depth_info_sub], 10)
        ts.registerCallback(self.callback)

        self.running = True

        self.startTime = time.time()
        rospy.spin()



    def callback(self, color_image, color_info, depth_image, depth_info):
        #print("Neine")
        self.colorImage = color_image

        try:
            self.img = self.bridge.imgmsg_to_cv2(self.colorImage, "bgr8")
            self.pilImg = PILImage.fromarray(self.img)
        except CvBridgeError as e:
            print(e)



        self.detection()
        #print(self.detection_info_msg)

        #self.viewer(self.img)
        self.detection_info_msg.header.stamp = color_image.header.stamp
        self.pub_detection.publish(self.detection_info_msg)
        self.pub_color_image.publish(color_image)
        self.pub_color_info.publish(color_info)
        self.pub_depth_image.publish(depth_image)
        self.pub_depth_info.publish(depth_info)



    def close(self):
        self.yolo.close_session()
        self.video.release()
        cv2.destroyAllWindows()
        rospy.signal_shutdown('Quitting')

    def viewer(self, img):


        if self.running:
            if not self.video.isOpened():
                print("error with writer")
            else:
                self.video.write(img)

        key = cv2.waitKey(1)
        if key == 113:
            self.close()


        cv2.imshow("get_image", img)

    def detection(self):



        image = self.pilImg

        #boxes har verdiene top, left, bottom, right

        (image, boxes, scores, classes) = self.yolo.detect_image(image)
        print(boxes)
        result = np.asarray(image) #Konverterer bildet slik at den kan brukes i openCV

        #Assign to message
        if len(classes) > 0:
            self.detection_info_msg.class_type = classes[0]
            self.detection_info_msg.score = scores[0]
            self.detection_info_msg.y1 = boxes[0][0]
            self.detection_info_msg.x1 = boxes[0][1]
            self.detection_info_msg.y2 = boxes[0][2]
            self.detection_info_msg.x2 = boxes[0][3]
            print("element 0: %d element 1: %d element 2: %d element 3: %d" % (boxes[0][0], boxes[0][1], boxes[0][2] ,boxes[0][3]) )
        else:
            self.detection_info_msg.class_type = -1

        #print(self.detection_info_msg.class_type)

        """"
        curr_time = timer()
        exec_time = curr_time - self.prev_time

        self.prev_time = curr_time
        self.accum_time = self.accum_time + exec_time
        self.curr_fps = self.curr_fps + 1
        if self.accum_time > 1:
            self.accum_time = self.accum_time -1
            self.fps = "FPS: " + str(self.curr_fps)
            self.curr_fps = 0
      """
        #cv2.putText(result, text=self.fps, org=(3,15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=(255,255,255), thickness=2)
        #cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        key = cv2.waitKey(1)
        if key == 113:
            self.close()









def main(args):
   ic = Receiver(args)



   rospy.init_node("Receiver", anonymous=True)

   try:
       ic.start()
   except KeyboardInterrupt:
       print("Shutting down")


   print(YOLO.get_defaults("model_path"))

def parser():
   parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
   '''
   Command line options
   '''
   parser.add_argument(
       '--model', type=str,
       help='path to model weight file, default ' + YOLO.get_defaults("model_path")
   )

   parser.add_argument(
       '--anchors', type=str,
       help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
   )

   parser.add_argument(
       '--classes', type=str,
       help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
   )

   parser.add_argument(
       '--gpu_num', type=int,
       help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
   )

   parser.add_argument(
       '--image', default=True, action="store_true",
       help='Image detection mode, will ignore all positional arguments'
   )
   '''
   Command line positional arguments -- for video detection mode
   '''
   parser.add_argument(
       "--input", nargs='?', type=str,required=False,default='./path2your_video',
       help = "Video input path"
   )

   parser.add_argument(
       "--output", nargs='?', type=str, default="",
       help = "[Optional] Video output path"
   )

   return parser.parse_args()

if __name__ == "__main__":

   FLAGS = parser()
   print(vars(FLAGS))
   main(FLAGS)

