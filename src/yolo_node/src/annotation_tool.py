import os
import matplotlib.pyplot as plt
import cv2
import datetime as dt
import numpy as np
from matplotlib.widgets import RectangleSelector


object = {
    0: "box-end",
    1: "pin-end"
}


#global constants
img = None
tl_list = []
br_list = []
object_list = []
save = False
running = True
isSaved = False

currentDT = dt.datetime.now()
file_name = "annotation_"+"0" + str(currentDT.month) + "." + str(currentDT.day) + ":" + str(currentDT.hour)
print(file_name)
annotation_file = open(file_name, 'w')


image_folder = '/home/erlendb/Pictures/Masteroppgave_bilder/Data260219/Color'
image_path = None
savedir = '/home/erlendb/Programmering/keras_yolo3'
objType = True #True - 1 for pin-end, False-0 for box-end


def line_selec_callback(clk, rls):
    global tl_list
    global br_list
    global save

    if save:
        print("Lagret et objekt av typen %s" % object[int(objType)])
        tl_list.append((int(clk.xdata), int(clk.ydata)))
        br_list.append((int(rls.xdata), int(rls.ydata)))
        object_list.append(int(objType))
        save = False


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    global save
    global objType
    global isSaved
    if event.key == 'c':
        objType = not objType
        print("Current type:" + object[int(objType)])

    if event.key == 'b':
        save = True

    if event.key == 't':
        tl_list = []
        br_list = []
        object_list = []
        print("Resetted")
    if event.key == 'q':
        print(tl_list, br_list, object_list)
        write_txt_file(tl_list, br_list, object_list)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()

    if event.key == 'm':
        plt.close()
        if not isSaved:
            write_txt_file(tl_list, br_list, object_list)

        global running
        global annotation_fileq
        annotation_file.close()
        running = False


def toggle_selector(event):
    toggle_selector.RS.set_active(True)

def write_txt_file(tl, br, obj):
    tl_arr = np.asarray(tl)
    br_arr = np.asarray(br)
    obj_arr = np.asarray(obj)
    global annotation_file
    #print(obj_arr.shape[0])
    tot_arr = np.empty([obj_arr.shape[0], 5])
    #print(tot_arr)
    #print(tl_arr.shape)
    print("topleft: %s\n bottomright: %s" % (str(tl_arr), str(br_arr)))

    for g in range(0, tl_arr.shape[0]):
        for h in range(0, 2):
            if tl_arr[g,h] > br_arr[g,h]:
                temp_arr = tl_arr
                tl_arr[g,h] = br_arr[g,h]

    print("topleft: %s\n bottomright: %s" % (str(tl_arr), str(br_arr)))

    annotation_file.write(str(image_path) + " ")

    k = 0
    for j in range(0, obj_arr.shape[0]):
        for i in range(0, 5):

            if i <= 1:
                tot_arr[j, i] = tl_arr[j, k]
                k += 1
            elif i > 1 and i <= 3:
                tot_arr[j, i] = br_arr[j, k]
                k += 1
            elif i == 4:
                tot_arr[j, i] = obj_arr[j]
                k = 0

            if k == 2:
                k = 0

            if i != 4:
                annotation_file.write(str(int(tot_arr[j, i]))+",")
            else:
                annotation_file.write(str(int(tot_arr[j, i])) + " ")
    annotation_file.write("\n")
    print(tot_arr)







if __name__ == '__main__':



    for n, image_file in enumerate(os.scandir(image_folder)):
        image_path = str(image_file.path)

        img = image_file
        fig, ax = plt.subplots(1, figsize=(15,9))

        mngr = plt.get_current_fig_manager()
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        print("Currently chosen class: %s" % object[objType])

        toggle_selector.RS = RectangleSelector(
            ax, line_selec_callback,
            drawtype='box', useblit=False,
            button =[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )

        if not running:
            print("hei")
            break

        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()