# single track for each person in each camera: tin, tout, xin, xout
import re

sngl_trck = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/single_tracks.txt")
single_tracks = []
for line in sngl_trck.readlines():
    if line.startswith("1") or line.startswith("2"):
        cam = [int(s) for s in re.findall(r'\d+', line)][0]
        id = [int(s) for s in re.findall(r'\d+', line)][1]
        frame_in = [int(s) for s in re.findall(r'\d+', line)][2]
        hour_in = [int(s) for s in re.findall(r'\d+', line)][3]
        min_in = [int(s) for s in re.findall(r'\d+', line)][4]
        sec_in = [int(s) for s in re.findall(r'\d+', line)][5]
        frame_out = [int(s) for s in re.findall(r'\d+', line)][6]
        hour_out = [int(s) for s in re.findall(r'\d+', line)][7]
        min_out = [int(s) for s in re.findall(r'\d+', line)][8]
        sec_out = [int(s) for s in re.findall(r'\d+', line)][9]
        x_in = [int(s) for s in re.findall(r'\d+', line)][10]
        x_out = [int(s) for s in re.findall(r'\d+', line)][11]
        single_tracks.append((cam, id, min_in, sec_in, min_out, sec_out, x_in, x_out))



candidate_subproblems = [(1, 1, 2, 1), (2, 3, 11, 1), (2, 2, 22, 2), (14, 1, 15, 1), (2, 4, 12, 1, 3, 1, 14, 4), (13, 4, 22, 1, 11, 2, 21, 3, 21, 4), (14, 5, 17, 1, 18, 1), (17, 3, 18, 3, 19, 5, 20, 3), (19, 1, 21, 1, 20, 1)]

for i in range(0, len(candidate_subproblems)):
    length = len(candidate_subproblems)

    if length == 4:
        cansub_cam_1 = candidate_subproblems[i][0]
        cansub_inout_1 = candidate_subproblems[i][1]
        cansub_cam_2 = candidate_subproblems[i][2]
        cansub_inout_2 = candidate_subproblems[i][3]
    elif length == 6:
        cansub_cam_1 = candidate_subproblems[i][0]
        cansub_inout_1 = candidate_subproblems[i][1]
        cansub_cam_2 = candidate_subproblems[i][2]
        cansub_inout_2 = candidate_subproblems[i][3]
        cansub_cam_3 = candidate_subproblems[i][4]
        cansub_inout_3 = candidate_subproblems[i][5]
    elif length == 8:
        cansub_cam_1 = candidate_subproblems[i][0]
        cansub_inout_1 = candidate_subproblems[i][1]
        cansub_cam_2 = candidate_subproblems[i][2]
        cansub_inout_2 = candidate_subproblems[i][3]
        cansub_cam_3 = candidate_subproblems[i][4]
        cansub_inout_3 = candidate_subproblems[i][5]
        cansub_cam_4 = candidate_subproblems[i][6]
        cansub_inout_4 = candidate_subproblems[i][7]
    elif length == 10:
        cansub_cam_1 = candidate_subproblems[i][0]
        cansub_inout_1 = candidate_subproblems[i][1]
        cansub_cam_2 = candidate_subproblems[i][2]
        cansub_inout_2 = candidate_subproblems[i][3]
        cansub_cam_3 = candidate_subproblems[i][4]
        cansub_inout_3 = candidate_subproblems[i][5]
        cansub_cam_4 = candidate_subproblems[i][6]
        cansub_inout_4 = candidate_subproblems[i][7]
        cansub_cam_5 = candidate_subproblems[i][8]
        cansub_inout_5 = candidate_subproblems[i][9]


cameras_fps_times = [(1, 18, 122725), (2, 25, 122700), (11, 18, 122725), (12, 25, 122700), (13, 25, 122700),
                         (14, 25, 122700), (15, 18, 122725), (17, 25, 122700), (18, 25, 122700), (19, 25, 122700),
                         (20, 25, 122700), (21, 18, 122725), (22, 25, 122700)]


print(single_tracks)



corrected_ST = []

for i in range(0, len(single_tracks)):
    if single_tracks[i][0] in (1, 11, 15, 21):
        if single_tracks[i][3] >= 25:
            new_m_in = single_tracks[i][2]
            new_s_in = single_tracks[i][3] - 25
        else:
            new_m_in = single_tracks[i][2] - 1
            new_s_in = 60 - (abs(single_tracks[i][3] - 25))

        if single_tracks[i][5] >= 25:
            new_m_out = single_tracks[i][4]
            new_s_out = single_tracks[i][5] - 25
        else:
            new_m_out = single_tracks[i][4] - 1
            new_s_out = 60 - (abs(single_tracks[i][5] - 25))

    else:
        new_m_in = single_tracks[i][2]
        new_s_in = single_tracks[i][3]
        new_m_out = single_tracks[i][4]
        new_s_out = single_tracks[i][5]

    corrected_ST.append((single_tracks[i][0], single_tracks[i][1], new_m_in, new_s_in, new_m_out, new_s_out, single_tracks[i][6], single_tracks[i][7]))

print(corrected_ST)



