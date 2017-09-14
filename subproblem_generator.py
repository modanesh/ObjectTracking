# ag: activity graph
# sct: set of single camera tracks SCT, SCT(i) = (tId, cId, e_in, e_out, t_in, t_out)

# def subproblem_generator(ag, sct):
#     IT = []
#     OT = []
#     S = []
#
#     t_inout_1 = []
#     for i in range(0, len(sct)):
#         t_inout_1.append((sct[i][4], sct[i][5]))
#
#     t_inout_2 = list(set(t_inout_1))
#     t_inout = sorted(t_inout_2, key = lambda x: (x[1], x[2]))
#
#     for t in t_inout:
#         for j in range(0, len(sct)):
#             if sct[j][4] == t[0]:
#                 IT.append((sct[j][1], sct[j][2], sct[j][0]))
#
#
#             if sct[j][5] == t[1]:
#                 OT.append((sct[j][1], sct[j][3], sct[j][0]))
#
#
#     S.append()
import re


def subproblem_generator(sct):
    it = []
    ot = []
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

                    if (sct[i][1] == correlations[k][0] and sct[i][3] == correlations[k][1] and sct[j][1] == correlations[k][2] and sct[j][3] == correlations[k][3]) or (sct[i][1] == correlations[k][2] and sct[i][3] == correlations[k][3] and sct[j][1] == correlations[k][0] and sct[j][3] == correlations[k][1]):
                        s.append((sct[i], sct[j]))


if __name__ == '__main__':
    subproblem_generator()