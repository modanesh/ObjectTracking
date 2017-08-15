import colorsys
from collections import Counter
from PIL import Image, ImageDraw
import cv2
from colorthief import ColorThief
from numpy import mean
import os
import numpy as np
from matplotlib import pyplot as plt



def extract_frames(path):
    """
    saves frames from the video.

    :param path: path to the video
    """
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        cv2.imwrite("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/frames/frame%d.jpeg" % count, image)
        count += 1


def extract_big_pedestrians(id):
    """
    extract pedestrians with BIG BOUNDING BOXES from images using a line of annotation file. saves cropped frames containing only the upper-body of pedestrians.

    :param id: person id in the annotation file
    """
    count = 0

    # loop over all the persons and crop their photo
    for line in range(3, len(lines)):

        if str(id) == lines[line].split("\t")[3] and count < 10:
            if lines[line].split("\t")[11] == str(1):
                if int(lines[line].split("\t")[7]) > 40 and int(lines[line].split("\t")[8]) > 90:
                    pedestrian_x = lines[line].split("\t")[5]
                    pedestrian_y = lines[line].split("\t")[6]
                    pedestrian_width = lines[line].split("\t")[7]
                    pedestrian_height = lines[line].split("\t")[8]
                    frame_number = lines[line].split("\t")[10]


                    print("line: " + str(line))
                    print("id: " + str(id))
                    print("fn: " + str(frame_number))
                    print("h: " + str(lines[line].split("\t")[7]))


                    img = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/frames/frame%d.jpeg" % int(frame_number))

                    img2 = img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))

                    width, height = img2.size
                    shirt = int(height/5)
                    img2 = img2.crop((0, shirt, width, shirt*3))

                    img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/cropped_frames/cropped_frame" + "_" + str(id) + "_" + frame_number + ".jpg")

                    count += 1

                    # keep persons who have big bounding boxes
                    if id not in big_box_ids:
                        big_box_ids.append(id)


def extract_little_pedestrians(id):
    """
        extract pedestrians with LITTLE BOUNDING BOXES from images using a line of annotation file. saves cropped frames containing only the upper-body of pedestrians.

        :param id: person id in the annotation file
        """
    count = 0

    # loop over persons who have a little bounding boxes and crop their photos
    for line in range(3, len(lines)):
        if str(id) == lines[line].split("\t")[3] and count < 10:
            if lines[line].split("\t")[3] not in str(big_box_ids):
                if lines[line].split("\t")[11] == str(1):
                        if int(lines[line].split("\t")[7]) > 40 or int(lines[line].split("\t")[8]) > 120:
                            pedestrian_x = lines[line].split("\t")[5]
                            pedestrian_y = lines[line].split("\t")[6]
                            pedestrian_width = lines[line].split("\t")[7]
                            pedestrian_height = lines[line].split("\t")[8]
                            frame_number = lines[line].split("\t")[10]

                            print("line: " + str(line))
                            print("id: " + str(id))
                            print("fn: " + str(frame_number))
                            print("h: " + str(lines[line].split("\t")[7]))

                            img = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/frames/frame%d.jpeg" % int(frame_number))

                            img2 = img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))

                            width, height = img2.size
                            shirt = int(height/5)
                            img2 = img2.crop((0, shirt, width, shirt*3))

                            img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/cropped_frames/cropped_frame" + "_" + str(id) + "_" + frame_number + ".jpg")

                            count += 1


def calculate_median_cut_RGB(path):
    """
    calculates the dominant colors in an image using the median cut algorithm, which
    is a sort of averaging pixel values.

    :param path: path to image
    :return: tuple of AVERAGING DOMINANT colors in an image in RGB
    """
    color_thief = ColorThief(path)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    return dominant_color


def calculate_histogram(path):
    """
    calculates the histogram of colors in an image, in RGB channels.

    :param path: path to image
    :return: tuple of HISTOGRAM colors in an image in RGB
    """
    img = cv2.imread(path)

    histogram_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    histogram_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    histogram_r = cv2.calcHist([img], [2], None, [256], [0, 256])
    image_hist = []
    image_hist.append((histogram_r.tolist().index(np.amax(histogram_r)), histogram_g.tolist().index(np.amax(histogram_g)), histogram_b.tolist().index(np.amax(histogram_b))))

    return image_hist


def calculate_most_frequent_color(path):
    """
        calculates the most frequent RGB colors in pixels of an image.

        :param path: path to image
        :return: tuple of HISTOGRAM colors in an image in RGB
        """
    image = Image.open(path)

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]


def hue_from_image(path):
    img = Image.open(path)
    r,g,b = img.split()
    Hdat = []
    Sdat = []
    Vdat = []
    for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
        h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
        Hdat.append(int(h*255.))
        Sdat.append(int(s*255.))
        Vdat.append(int(v*255.))

    return Hdat


def hue_from_rgb(colors):
    red, green, blue = colors
    Hdat = []
    Sdat = []
    Vdat = []
    h, s, v = colorsys.rgb_to_hsv(red/255., green/255., blue/255.)
    Hdat.append(int(h*255.))
    Sdat.append(int(s*255.))
    Vdat.append(int(v*255.))

    return Hdat


def id_in_frames(id, camera_id):
    """

    :param id: get the id of pedestrian
    :return: average dominant color of the person in 10 different frames
    """
    id_dominant_colors = []
    path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/"+str(camera_id)+"/foreground/"
    for filename in os.listdir(path):
        # print(filename.startswith("cropped_frame_" + str(id)))
        if filename.startswith("cropped_frame_" + str(id) + "_") and filename.endswith(".jpg"):
            print(filename)
            dominant_color = calculate_median_cut_RGB(path+filename)
            id_dominant_colors.append(dominant_color)

    average_dominant_color = mean(id_dominant_colors, axis=0).astype(int)
    print(id_dominant_colors)
    print(average_dominant_color)


    return average_dominant_color


def color_similarity_evaluation(first_color, second_color):
    print("evaluate")
    difference = abs(first_color - second_color)

    # TODO check 10 is ok or not
    if difference < 10:
        return True
    else:
        return False



def color_similarity_calculator(color_array):
    print("ed")
    print(color_array[0])
    print(color_array[0][0])
    print(color_array[0][1])
    print(color_array[0][2])



    hh1 = hue_from_rgb(color_array[0][2])
    hh2 = hue_from_rgb(color_array[1][2])

    print(hh1)
    print(hh2)

    same = color_similarity_evaluation(hh1[0], hh2[0])

    print(same)



if __name__ == '__main__':

    ann_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/19.txt", "r")
    lines = ann_file.readlines()
    id_camera_color = []
    big_box_ids = []
    average_all_colors = []
    cameras = [1, 2, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22]

    # extract_frames("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/19.m4v")

    # for i in range(1, 11):
    #     extract_big_pedestrians(i)

    # for i in range(1, 11):
    #     extract_little_pedestrians(i)

    # file = open("colors.txt", "a")
    # camera_id = 19
    #
    # for i in range(1, 11):
    #     average_color = id_in_frames(i, camera_id)
    #     average_all_colors.append((i, average_color))
    #     id_camera_color.append((camera_id, i, average_color))
    #
    # file.write(str(id_camera_color)+"\n")
    # file.close()
    #
    #
    # color_similarity_calculator(id_camera_color)

