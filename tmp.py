file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
file2 = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp2.txt", "w")


for line in file.readlines():
    print(line)
    stss = "(" +line
    print(stss)
    file2.write(stss)