from math import sqrt

import numpy as np
from scipy.spatial import distance

first_column = np.array(((20, 22, 27), (148, 142, 174), (118, 103, 80), (73, 74, 88), (79, 74, 45), (91, 70, 43), (81, 77, 91),
                (145, 141, 148), (65, 59, 72), (147, 141, 149), (72, 85, 94), (90, 88, 104), (75, 96, 106), (92, 86, 93),
                (76, 73, 86), (76, 86, 82), (72, 67, 81), (91, 89, 106), (98, 95, 106), (147, 141, 149), (140, 96, 116),
                (140, 96, 116), (175, 172, 190), (62, 56, 62), (79, 72, 77), (73, 67, 71)))


second_column = np.array(((61, 70, 77), (58, 70, 89), (80, 85, 96), (92, 104, 115), (71, 84, 98), (102, 98, 110), (124, 126, 143),
                (128, 136, 157), (147, 154, 144), (128, 136, 157), (67, 103, 95), (80, 86, 97), (65, 104, 95), (106, 108, 104),
                (57, 57, 66), (77, 111, 69), (79, 81, 98), (86, 88, 108), (63, 68, 85), (175, 172, 190), (175, 172, 190),
                (102, 93, 98), (102, 93, 98), (123, 170, 236), (155, 210, 251), (98, 92, 125)))

distances = []
for i in range(0, len(first_column)):
    first_dif = first_column[i][0] - second_column[i][0]
    second_dif = first_column[i][1] - second_column[i][1]
    thirs_dif = first_column[i][2] - second_column[i][2]
    distances.append(int(distance.euclidean(first_column[i], second_column[i])))

heus = np.array((11, 24, 131, 20, 113, 161, 17, 36, 117, 43, 26, 20, 24, 143, 9, 34, 20, 9, 21, 24, 58, 4, 54, 60, 79, 49))

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
for i in range(0, len(distances)):
    # print(distances[i], heus[i])
    if distances[i] < 20 and heus[i] < 20:
        count_1 += 1
        

    elif distances[i] < 30 and heus[i] < 30:
        count_2 += 1
        

    elif distances[i] < 40 and heus[i] < 40:
        count_3 += 1
        

    elif distances[i] < 50 and heus[i] < 50:
        count_4 += 1
        

    elif distances[i] < 50 and heus[i] < 25:
        count_5 += 1
        

    elif distances[i] < 50 and heus[i] < 35:
        count_6 += 1
        

    elif distances[i] < 50 and heus[i] < 45:
        count_7 += 1
        

print(count_1)
print(count_2)
print(count_3)
print(count_4)
print(count_5)
print(count_6)
print(count_7)