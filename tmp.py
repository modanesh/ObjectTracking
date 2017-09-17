import re

import os

path = "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/better_foreground/"

for filename in os.listdir(path):

    h = [int(s) for s in re.findall(r'\d+', filename)]

    print(h)