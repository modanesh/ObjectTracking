from PIL import Image, ImageDraw
import cv2
from matplotlib import patches
import matplotlib.pyplot as plt
from colorthief import ColorThief

def extract_frames(path):
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        cv2.imwrite("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/resources/frames/frame%d.jpeg" % count, image)
        count += 1


def extract_pedestrians(line):
    ll = lines[line].split("\t")
    pedestrian_x = ll[5]
    pedestrian_y = ll[6]
    pedestrian_width = ll[7]
    pedestrian_height = ll[8]
    frame_number = ll[10]
    print(pedestrian_x)
    print(pedestrian_y)
    print(pedestrian_width)
    print(pedestrian_height)
    print(frame_number)


    img = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/frame%d.jpeg" % int(frame_number))

    img2 = img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))


    width, height = img2.size
    shirt = int(height/5)
    img2 = img2.crop((0, shirt, width, shirt*3))

    img2.save("cropped_frame" + frame_number + ".jpg")

    color_thief = ColorThief('/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/cropped_frame' + frame_number + '.jpg')
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    print("dominant color(in RGB): " + str(dominant_color))


def select_frames():
    pedestrian_ids_frames = []
    for i in range(3,len(lines)):
        id = lines[i].split("\t")[3]
        fnumber = lines[i].split("\t")[10]

        pedestrian_ids_frames.append([id, fnumber])

    print(len(pedestrian_ids_frames))

    count = 0
    first_id = pedestrian_ids_frames[0][0]
    # for j in range(len(pedestrian_ids_frames)):
        # if pedestrian_ids_frames[0][j] == first_id:



ann_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/resources/1.txt", "r")
lines = ann_file.readlines()
extract_pedestrians(3)
select_frames()
print(len(lines))

color_thief = ColorThief("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/a.png")
# get the dominant color
dominant_color = color_thief.get_color(quality=1)

print("dominant color(in RGB): " + str(dominant_color))