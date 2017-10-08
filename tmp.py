import re

file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")

# a_2_4_in = [21,
# 26,
# 27,
# 33,
# 45,
# 46,
# 50,
# 51,
# 8]

# a_2_4_out = [14,
# 1,
# 20,
# 24,
# 28,
# 2,
# 31,
# 36,
# 37,
# 6]

b = []

for line in file.readlines():
    cam_1 = [int(s) for s in re.findall(r'\d+', line)][0]
    id_1 = [int(s) for s in re.findall(r'\d+', line)][1]
    cam_2 = [int(s) for s in re.findall(r'\d+', line)][2]
    id_2 = [int(s) for s in re.findall(r'\d+', line)][3]
    if cam_1 == 2 and cam_2 == 13:
        if id_1 in a and id_2 in b:
            file2.write(line)
    else:
        file2.write(line)
