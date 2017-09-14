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


def subproblem_generator(ag, sct):
    it = []
    ot = []
    s = []

    for i in range(0, len(sct)):
        for j in range(0, len(sct)):
            if sct[i][5] == sct[j][4]:
                s.append((sct[i][1], sct[i][2], sct[i][3], sct[i][4], sct[i][5], sct[j][1], sct[j][2], sct[j][3], sct[j][4], sct[j][5]))





def camera_connections(camera_tracks):

    file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/camera_correlations.txt")

    correlations = []
    subproblems = []

    for line in file.readlines():
        correlations.append(([int(s) for s in re.findall(r'\d+', line)][0], [int(s) for s in re.findall(r'\d+', line)][1]))

    print(correlations)

    for i in range(0, len(camera_tracks)):
        for j in range(0, len(correlations)):
            first_cam = correlations[j][0]
            second_cam = correlations[j][1]

            if (camera_tracks[i][0] == first_cam and camera_tracks[i][5] == second_cam) or (camera_tracks[i][0] == second_cam and camera_tracks[i][5] == first_cam):
                subproblems.append(camera_tracks[i])




if __name__ == '__main__':
    camera_connections()