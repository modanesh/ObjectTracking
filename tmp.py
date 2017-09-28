import re

import os

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
lines = file.readlines()

file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")


print(lines)
print([int(s) for s in re.findall(r'\d+', lines[0])][0])
print([int(s) for s in re.findall(r'\d+', lines[0])][1])
print([int(s) for s in re.findall(r'\d+', lines[0])][2])

for i in range(0, len(lines)):
    if [int(s) for s in re.findall(r'\d+', lines[i])][0] == [int(s) for s in re.findall(r'\d+', lines[i+1])][0] and [int(s) for s in re.findall(r'\d+', lines[i])][1] == [int(s) for s in re.findall(r'\d+', lines[i+1])][1]:

        inouts = str([int(s) for s in re.findall(r'\d+', lines[i])][0]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i])][1]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i])][2]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i])][3]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i])][4]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i])][5]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i+1])][2]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i+1])][3]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i+1])][4]) + ", " + str([int(s) for s in re.findall(r'\d+', lines[i+1])][5]) + "\n"

        file2.write(inouts)