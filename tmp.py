import re

import os

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
lines = file.readlines()
file.close()

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")

arr1 = [11,
18,
19,
20,
26,
7]
arr2 = [1]
print(len(arr1)*len(arr2))

for line in lines:
    cam1 = [int(s) for s in re.findall(r'\d+', line)][0]
    id1 = [int(s) for s in re.findall(r'\d+', line)][1]
    cam2 = [int(s) for s in re.findall(r'\d+', line)][2]
    id2 = [int(s) for s in re.findall(r'\d+', line)][3]

    if cam1 == 21 and cam2 == 11 and id1 in arr1 and id2 in arr2:
        print("eh")
        print(cam1, id1, cam2, id2)

    else:
        file.write(line)