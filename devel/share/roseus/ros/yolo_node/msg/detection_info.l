;; Auto-generated. Do not edit!


(when (boundp 'yolo_node::detection_info)
  (if (not (find-package "YOLO_NODE"))
    (make-package "YOLO_NODE"))
  (shadow 'detection_info (find-package "YOLO_NODE")))
(unless (find-package "YOLO_NODE::DETECTION_INFO")
  (make-package "YOLO_NODE::DETECTION_INFO"))

(in-package "ROS")
;;//! \htmlinclude detection_info.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass yolo_node::detection_info
  :super ros::object
  :slots (_header _class_type _score _x1 _x2 _y1 _y2 ))

(defmethod yolo_node::detection_info
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:class_type __class_type) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:score __score) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:x1 __x1) (make-array 0 :initial-element 0 :element-type :integer))
    ((:x2 __x2) (make-array 0 :initial-element 0 :element-type :integer))
    ((:y1 __y1) (make-array 0 :initial-element 0 :element-type :integer))
    ((:y2 __y2) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _class_type __class_type)
   (setq _score __score)
   (setq _x1 __x1)
   (setq _x2 __x2)
   (setq _y1 __y1)
   (setq _y2 __y2)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:class_type
   (&optional __class_type)
   (if __class_type (setq _class_type __class_type)) _class_type)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:x1
   (&optional __x1)
   (if __x1 (setq _x1 __x1)) _x1)
  (:x2
   (&optional __x2)
   (if __x2 (setq _x2 __x2)) _x2)
  (:y1
   (&optional __y1)
   (if __y1 (setq _y1 __y1)) _y1)
  (:y2
   (&optional __y2)
   (if __y2 (setq _y2 __y2)) _y2)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string[] _class_type
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _class_type)) 4
    ;; float32[] _score
    (* 4    (length _score)) 4
    ;; int16[] _x1
    (* 2    (length _x1)) 4
    ;; int16[] _x2
    (* 2    (length _x2)) 4
    ;; int16[] _y1
    (* 2    (length _y1)) 4
    ;; int16[] _y2
    (* 2    (length _y2)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string[] _class_type
     (write-long (length _class_type) s)
     (dolist (elem _class_type)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float32[] _score
     (write-long (length _score) s)
     (dotimes (i (length _score))
       (sys::poke (elt _score i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; int16[] _x1
     (write-long (length _x1) s)
     (dotimes (i (length _x1))
       (write-word (elt _x1 i) s)
       )
     ;; int16[] _x2
     (write-long (length _x2) s)
     (dotimes (i (length _x2))
       (write-word (elt _x2 i) s)
       )
     ;; int16[] _y1
     (write-long (length _y1) s)
     (dotimes (i (length _y1))
       (write-word (elt _y1 i) s)
       )
     ;; int16[] _y2
     (write-long (length _y2) s)
     (dotimes (i (length _y2))
       (write-word (elt _y2 i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string[] _class_type
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _class_type (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _class_type i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float32[] _score
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _score (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _score i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; int16[] _x1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x1 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _x1 i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; int16[] _x2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x2 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _x2 i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; int16[] _y1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y1 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _y1 i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; int16[] _y2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y2 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _y2 i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get yolo_node::detection_info :md5sum-) "ea2d9911aca1cdbc2e7d80a7846b80e6")
(setf (get yolo_node::detection_info :datatype-) "yolo_node/detection_info")
(setf (get yolo_node::detection_info :definition-)
      "Header header
string[] class_type
float32[] score
int16[] x1
int16[] x2
int16[] y1
int16[] y2

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :yolo_node/detection_info "ea2d9911aca1cdbc2e7d80a7846b80e6")


