from collections import Counter
from PIL import Image, ImageDraw
import cv2
from colorthief import ColorThief
from numpy import mean
import os


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
        cv2.imwrite("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/frames/frame%d.jpeg" % count, image)
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


                    img = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/frames/frame%d.jpeg" % int(frame_number))

                    img2 = img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))

                    width, height = img2.size
                    shirt = int(height/5)
                    img2 = img2.crop((0, shirt, width, shirt*3))

                    img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/cropped_frames/cropped_frame" + "_" + str(id) + "_" + frame_number + ".jpg")

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

                        print(line)
                        print(lines[line].split("\t")[3])
                        print(str(big_box_ids))
                        print(lines[line].split("\t")[3] not in str(big_box_ids))

                        img = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/frames/frame%d.jpeg" % int(frame_number))

                        img2 = img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))

                        width, height = img2.size
                        shirt = int(height/5)
                        img2 = img2.crop((0, shirt, width, shirt*3))

                        img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/cropped_frames/cropped_frame" + "_" + str(id) + "_" + frame_number + ".jpg")

                        count += 1


def extract_RGB(path):
    """

    :param path: path to image
    :return: tuple of dominant colors in an images in RGB
    """
    color_thief = ColorThief(path)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    return dominant_color


def id_in_frames(id):
    """

    :param id: get the id of pedestrian
    :return: average dominant color of the person in 10 different frames
    """
    id_dominant_colors = []
    path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/cropped_frames/"
    for filename in os.listdir(path):
        # print(filename.startswith("cropped_frame_" + str(id)))
        if filename.startswith("cropped_frame_" + str(id) + "_") and filename.endswith(".jpg"):
            print(filename)
            dominant_color = extract_RGB(path+filename)
            id_dominant_colors.append(dominant_color)

    average_dominant_color = mean(id_dominant_colors, axis=0).astype(int)
    print(id_dominant_colors)
    print(average_dominant_color)


    return average_dominant_color




if __name__ == '__main__':

    ann_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/22.txt", "r")
    lines = ann_file.readlines()
    id_camera_color = []
    big_box_ids = []
    average_all_colors = []


    extract_frames("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/22.m4v")



    for i in range(1, 18):
        extract_big_pedestrians(i)
        # average_color = id_in_frames(i)
        # average_all_colors.append((i, average_color))
        # id_camera_color.append((i, 1, average_color))

    for i in range(1, 18):
        extract_little_pedestrians(i)

    print(average_all_colors)


