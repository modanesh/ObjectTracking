import re

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")

count = 0
for line in file.readlines():
    h = [int(s) for s in re.findall(r'\d+', line)][0]
    e = [int(s) for s in re.findall(r'\d+', line)][1]

    if e < 14:
        count += 1

print(count)