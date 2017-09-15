import re


def subproblem_generator(sct):
    s = []

    file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/camera_correlations.txt")
    correlations = []

    for line in file.readlines():
        if not line.startswith("#"):
            correlations.append(([int(s) for s in re.findall(r'\d+', line)][0], [int(s) for s in re.findall(r'\d+', line)][1], [int(s) for s in re.findall(r'\d+', line)][2], [int(s) for s in re.findall(r'\d+', line)][3]))

    for i in range(0, len(sct)):
        for j in range(0, len(sct)):
            for k in range(0, len(correlations)):
                if sct[i][5] == sct[j][4]:

                    if sct[i][1] == correlations[k][0] and sct[i][3] == correlations[k][1] and sct[j][1] == correlations[k][2] and sct[j][3] == correlations[k][3]:
                        s.append((0, sct[i], 1, sct[j]))
                    elif sct[i][1] == correlations[k][2] and sct[i][3] == correlations[k][3] and sct[j][1] == correlations[k][0] and sct[j][3] == correlations[k][1]:
                        s.append((0, sct[j], 1, sct[i]))


if __name__ == '__main__':
    # TODO: SCTs
    subproblem_generator()