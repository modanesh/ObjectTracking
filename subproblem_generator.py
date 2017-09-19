import re
import os
import numpy as np

file_1 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/camera_regions.txt")
cams_regions = []
for line in file_1.readlines():
    if re.match(r"\d", line):

        cam_1 = [int(s) for s in re.findall(r'\d+', line)][0]
        region_1 = [int(s) for s in re.findall(r'\d+', line)][1]
        cam_2 = [int(s) for s in re.findall(r'\d+', line)][2]
        region_2 = [int(s) for s in re.findall(r'\d+', line)][3]
        cams_regions.append((cam_1, region_1, cam_2, region_2))


file_2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/same_in_out.txt")
cams_inouts = []
for line in file_2.readlines():
    if re.match(r"\(\d", line):

        cam_1 = [int(s) for s in re.findall(r'\d+', line)][0]
        id_1 = [int(s) for s in re.findall(r'\d+', line)][1]
        cam_2 = [int(s) for s in re.findall(r'\d+', line)][2]
        id_2 = [int(s) for s in re.findall(r'\d+', line)][3]

        in_1 = [int(s) for s in re.findall(r'\d+', line)][4]
        out_1 = [int(s) for s in re.findall(r'\d+', line)][5]
        in_2 = [int(s) for s in re.findall(r'\d+', line)][6]
        out_2 = [int(s) for s in re.findall(r'\d+', line)][7]

        print("____________________")
        print(in_1)
        print(out_1)
        print(in_2)
        print(out_2)

        cams_inouts.append((cam_1, id_1, in_1, out_1, cam_2, id_2, in_2, out_2))



s_v1 = []
s_v1 = cams_regions

