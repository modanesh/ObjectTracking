import re

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")

in_12_1 = [10,11,15,16,18,19,1,21,22,23,24,25,26,2,6,7,8,9]
out_12_1 = [10,11,12,13,14,16,17,18,19,1,20,21,22,23,24,25,2,3,4,6,7,8,9]
in_13_1 = [10,11,13,14,17,18,19,1,20,21,22,24,25,26,2,30,31,32,33,34,35,3,4,5,8,9]
out_13_1 = [10,15,16,18,21,22,23,25,27,28,29,32,7,8,9]
in_14_4 = [1,11,12,14,15,18,19,20,24,26,32,33,34,35,37,3,47,48]
out_14_4 = [2 ,4 ,5 ,6 ,7 ,8 ,10,13,16,17,23,25,27,28,29,30,31,38,39,41,46,49,4]

in_14_1 = [10,22,25,31,38,41,49]
out_14_1 = [18,20,24,26,32,33,42,47]
in_15_1 = [11,14,15,4,5,6,7,9]
out_15_1 = [12,2,4,8]

in_14_5 = [2,4,6,7,8,13,17,27,28,30,39,43,44,45]
out_14_5 = [1,12,22,36,3,9]
in_17_1 = [17, 4, 8]
out_17_1 = [12,14,16,18,19,1 ,20,21,2,3,5]
in_18_1 = [2,7,8]
out_18_1 = [1,3,4,5,9]

for line in file.readlines():
    cam_1 = [int(s) for s in re.findall(r'\d+', line)][0]
    id_1 = [int(s) for s in re.findall(r'\d+', line)][1]
    cam_2 = [int(s) for s in re.findall(r'\d+', line)][2]
    id_2 = [int(s) for s in re.findall(r'\d+', line)][3]
    if cam_1 == 17 and cam_2 == 18:
        if id_1 in out_17_1 and id_2 in in_18_1:
            file2.write(line)
    else:
        file2.write(line)
