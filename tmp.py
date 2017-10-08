import re

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")

in_12_1 = [10,11,15,16,18,19,1,21,22,23,24,25,26,2,6,7,8,9]
out_12_1 = [10,11,12,13,14,16,17,18,19,1,20,21,22,23,24,25,2,3,4,6,7,8,9]
in_13_1 = [10,11,13,14,17,18,19,1,20,21,22,24,25,26,2,30,31,32,33,34,35,3,4,5,8,9]
out_13_1 = [10,15,16,18,21,22,23,25,27,28,29,32,7,8,9]

for line in file.readlines():
    cam_1 = [int(s) for s in re.findall(r'\d+', line)][0]
    id_1 = [int(s) for s in re.findall(r'\d+', line)][1]
    cam_2 = [int(s) for s in re.findall(r'\d+', line)][2]
    id_2 = [int(s) for s in re.findall(r'\d+', line)][3]
    if cam_1 == 12 and cam_2 == 13:
        if id_1 in out_12_1 and id_2 in in_13_1:
            file2.write(line)
    else:
        file2.write(line)
