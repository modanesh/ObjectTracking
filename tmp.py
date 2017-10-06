import re

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt")

a = []
b = [1]
c = [6]

file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt", "w")

for line in file.readlines():
    if [int(s) for s in re.findall(r'\d+', line)][0] == 17 and [int(s) for s in re.findall(r'\d+', line)][1] in a:
        if [int(s) for s in re.findall(r'\d+', line)][2] == 18 and [int(s) for s in re.findall(r'\d+', line)][3] in b:
            print("")
        # elif [int(s) for s in re.findall(r'\d+', line)][2] == 18 and [int(s) for s in re.findall(r'\d+', line)][3] in c:
        #     print("")
        else:
            file2.write(line)
    else:
        file2.write(line)
