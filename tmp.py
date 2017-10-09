file1 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt")

for line1 in file1.readlines():
    for line2 in file2.readlines():
        if line1 == line2:
            print(line1)
            print(line2)