from PIL import Image, ImageEnhance
from skimage import io
import numpy as np
import cv2
import os
# np.set_printoptions(threshold=np.nan)


def cropped_frames_bg():
    for id in range(1, 18):
    # id = 43
        #TODO
        annotation_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/22.txt", 'r')
        lines = annotation_file.readlines()

        # TODO
        bg_path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/Background/22.png"
        bg_img = Image.open(bg_path)
        id_frames = []
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

                        # TODO
                        cropped_img2.save("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/background_removed/background_removed_"+str(id)+"_"+lines[line].split("\t")[10]+".jpg")

                        count += 1



background = cv2.imread("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/cropped_frame_bg.png")
foreground = cv2.imread("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/cropped_frame_1_0.jpg")

fg = cv2.subtract(background, foreground)

cv2.imwrite("3.png", fg)


im = Image.open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/3.png")

scale_value = 2
contrast = ImageEnhance.Contrast(im)
contrast_applied = contrast.enhance(scale_value)

pixels = contrast_applied.getdata()

black_n_white = []

for pixel in pixels:
    if pixel == (0, 0, 0):
        black_n_white.append(pixel)
    else:
        black_n_white.append((255, 255, 255))

mask = Image.new("RGB", (60, 58))
mask.putdata(black_n_white)
mask.save('mask.jpg')

mask = cv2.imread("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/mask.jpg")

mask2 = np.where((mask < 200), 0, 1).astype('uint8')

background_removed = foreground * mask2

cv2.imwrite("background_removed.jpg", background_removed)
