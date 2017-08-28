import re
import numpy as np



a = re.findall(r'\d+', 'he1llo1 42 I\'m a 32 string 30')

print(a)

aa = [int(s) for s in re.findall(r'\d+', 'array[(98')]

print(aa)


meh = [(44, 28, 38), (36, 25, 35), (36, 28, 36), (36, 27, 34), (44, 31, 39), (36, 28, 36), (32, 26, 35), (32, 27, 35), (52, 34, 44), (39, 28, 44)]
# meh = [(20, 30, 50), (50, 60, 70), (260, 440, 110)]
# print(meh[0])
# print(meh[0][0])

heh = []

for i in range(0, len(meh)):
    if meh[i][0] > 30 and meh[i][0] < 225:
        if meh[i][1] > 30 and meh[i][1] < 225:
            if meh[i][2] > 30 and meh[i][2] < 225:
                heh.append(meh[i])
print(heh)
heh.append((52, 50, 30))
sortedd = sorted(heh, key=lambda l: (l[0],l[1],[2]), reverse=True)
print(sortedd)
