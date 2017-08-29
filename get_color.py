import os
import re

from PIL import Image, ImageDraw

def get_colors(infile, numcolors=10, swatchsize=20, resize=150):

    image = Image.open(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)
    dists = []
    counts = 0
    for i in range(0, len(colors)):
        if colors[i][1][0] > 20 or colors[i][1][1] > 20 or colors[i][1][2] > 20 :
            dist = abs(colors[i][1][0] - colors[i][1][1]) + abs(colors[i][1][0] - colors[i][1][2]) + abs(colors[i][1][1] - colors[i][1][2])
            dists.append((dist, colors[i][0], (colors[i][1][0], colors[i][1][1], colors[i][1][2])))
            counts += colors[i][0]
        else:
            # print("eh")
            counts += colors[i][0]

    sorted_dist = sorted(dists, key=lambda l: (l[0],l[1]), reverse=True)

    special_sorted_dist = []
    for index in range(0, len(sorted_dist)):
        if sorted_dist[0][0] < 20:
            if sorted_dist[index][0] > 15 and sorted_dist[index][1]/counts > 0.1:
                special_sorted_dist.append(sorted_dist[index])
            else:
                special_sorted_dist.append("0")
        else:
            special_sorted_dist.append("0")

    if sorted_dist[0] == special_sorted_dist[0] or special_sorted_dist[0] != 0:

        return sorted_dist[0]

    else:

        return special_sorted_dist[0]



if __name__ == '__main__':
    path = '/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/22/better_foreground/'
    file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/colors_from_betters/colors_22.txt", "w")
    dom_color = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            id = [int(s) for s in re.findall(r'\d+', filename)][0]
            dom_color.append((22, id, get_colors(path + filename)[2]))
            file.write(str((22, id, get_colors(path + filename)[2])) + "\n")

    print(dom_color)



    file.close()