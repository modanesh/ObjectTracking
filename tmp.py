import re

file1 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt")

lines1 = file1.readlines()
lines2 = file2.readlines()

for i in range(0, len(lines1)):
    cam11 = [int(s) for s in re.findall(r'\d+', lines1[i])][0]
    id11 = [int(s) for s in re.findall(r'\d+', lines1[i])][1]
    cam12 = [int(s) for s in re.findall(r'\d+', lines1[i])][2]
    id12 = [int(s) for s in re.findall(r'\d+', lines1[i])][3]

    for j in range(0, len(lines2)):
        cam21 = [int(s) for s in re.findall(r'\d+', lines2[j])][0]
        id21 = [int(s) for s in re.findall(r'\d+', lines2[j])][1]
        cam22 = [int(s) for s in re.findall(r'\d+', lines2[j])][2]
        id22 = [int(s) for s in re.findall(r'\d+', lines2[j])][3]



        if cam11 == cam21 and id11 == id21 and cam12 == cam22 and id12 == id22:
            print(lines1[i])
            print(lines2[j])



