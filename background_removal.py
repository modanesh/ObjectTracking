import glob

from PIL import Image, ImageEnhance
from skimage import io
import numpy as np
import cv2
import os
# np.set_printoptions(threshold=np.nan)


def cropped_frames_bg():
    for id in range(1, 11):
        annotation_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/19.txt", 'r')
        lines = annotation_file.readlines()

        bg_path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/Background/19.png"
        bg_img = Image.open(bg_path)
        count = 0

        for line in range(3, len(lines)):
            if str(id) == lines[line].split("\t")[3] and count < 10:
                if lines[line].split("\t")[11] == str(1):
                    if int(lines[line].split("\t")[7]) > 40 and int(lines[line].split("\t")[8]) > 90:
                    # if int(lines[line].split("\t")[7]) > 40 or int(lines[line].split("\t")[8]) > 120:

                        x = lines[line].split("\t")[5]
                        y = lines[line].split("\t")[6]
                        w = lines[line].split("\t")[7]
                        h = lines[line].split("\t")[8]

                        cropped_img = bg_img.crop((int(x), int(y), int(x)+int(w), int(y)+int(h)))

                        width, height = cropped_img.size

                        shirt = int(height / 5)

                        cropped_img2 = cropped_img.crop((0, shirt, width, shirt * 3))

                        cropped_img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/19/background/background_removed_"+str(id)+"_"+lines[line].split("\t")[10]+".jpg")

                        count += 1



def better_cropped_frames_bg(id, path, bg_path):
    bg_img = Image.open(bg_path)

    bbox_size = []

    # loop over all the persons and crop their photo
    for line in range(3, len(lines)):

        if str(id) == lines[line].split("\t")[3]:
            if lines[line].split("\t")[11] == str(1):
                x = int(lines[line].split("\t")[5])
                y = int(lines[line].split("\t")[6])
                width = int(lines[line].split("\t")[7])
                height = int(lines[line].split("\t")[8])
                frame = int(lines[line].split("\t")[10])
                area = width * height
                bbox_size.append((x, y, width, height, line, frame, area))

    sorted_bbox = sorted(bbox_size, key=lambda l: l[6], reverse=True)

    for index in range(0, len(sorted_bbox)):
        if sorted_bbox[index][6] > 6500 and index < 1:
            print(sorted_bbox[index][6])
            pedestrian_x = sorted_bbox[index][0]
            pedestrian_y = sorted_bbox[index][1]
            pedestrian_width = sorted_bbox[index][2]
            pedestrian_height = sorted_bbox[index][3]
            frame_number = sorted_bbox[index][5]

            cropped_img = bg_img.crop((int(pedestrian_x), int(pedestrian_y), int(pedestrian_width)+int(pedestrian_x), int(pedestrian_height)+int(pedestrian_y)))

            half_width, half_height = cropped_img.size
            shirt = int(half_height / 5)
            cropped_img2 = cropped_img.crop((0, shirt, half_width, shirt * 3))

            cropped_img2.save(path + "/better_background/background_removed_" + str(id) + "_" + str(frame_number) + ".jpg")



def extract_foreground(background_path, foreground_path):
    background = cv2.imread(background_path)
    foreground = cv2.imread(foreground_path)

    fg = cv2.subtract(background, foreground)

    cv2.imwrite("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/temp/3.png", fg)


    im = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/temp/3.png")

    scale_value = 1.5
    contrast = ImageEnhance.Contrast(im)
    contrast_applied = contrast.enhance(scale_value)

    pixels = contrast_applied.getdata()

    black_n_white = []

    for pixel in pixels:
        if pixel == (0, 0, 0):
            black_n_white.append(pixel)
        else:
            black_n_white.append((255, 255, 255))

    mask_shape = foreground.shape
    mask = Image.new("RGB", (mask_shape[1], mask_shape[0]))
    mask.putdata(black_n_white)
    mask.save('/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/temp/mask.jpg')

    mask = cv2.imread("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/temp/mask.jpg")

    mask2 = np.where((mask < 200), 0, 1).astype('uint8')

    background_removed = foreground * mask2

    filename = foreground_path.split("/")[-1]
    cv2.imwrite("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/better_foreground/"+filename, background_removed)



if __name__ == '__main__':
    ann_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/22.txt", "r")
    lines = ann_file.readlines()
    path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22"
    bg_path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/Background/22.png"

    # for i in range(1, 80):
    #     print("-----------")
    #     print(i)
    #     better_cropped_frames_bg(i, path, bg_path)


    count = 0
    bg_files = glob.glob("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/better_background/*.jpg")
    fg_files = glob.glob("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/better_cropped_frames/*.jpg")
    for i in range(0, len(bg_files)):
        extract_foreground(bg_files[i], fg_files[i])
