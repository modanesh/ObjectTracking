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


# (1, 10, 27, 27, 27, 42, 2, 1)
# (2, 20, 27, 43, 27, 48, 1, 4)


# (1, 10, 27, 27, 27, 58, 2, 1)
# (2, 20, 28, 2, 27, 48, 1, 4)

threshold = 5
for i in range(0, len(corrected_ST)):
    for j in range(0, len(corrected_ST)):
        if corrected_ST[i][0] == 1 and corrected_ST[i][7] == 1:
            if corrected_ST[j][0] == 2 and corrected_ST[j][6] == 1:
                if corrected_ST[i][4] == corrected_ST[j][2]:
                    if corrected_ST[j][3] - corrected_ST[i][5] < threshold and corrected_ST[j][3] > corrected_ST[i][5]:
                        print("hi")
                        print(corrected_ST[i][4], corrected_ST[i][5])
                        print(corrected_ST[j][2], corrected_ST[j][3])
                        print(corrected_ST[i])
                        print(corrected_ST[j])
                elif corrected_ST[j][2] - corrected_ST[i][4] == 1:
                    if (corrected_ST[j][3] + 60) - corrected_ST[i][5] < threshold:
                        print("ih")
                        print(corrected_ST[i])
                        print(corrected_ST[j])



sorted_corrected_ST = sorted(corrected_ST, key=lambda l: (l[4],l[5]), reverse=False)
cam1_sorted_st = []
cam2_sorted_st = []
cam11_sorted_st = []
cam12_sorted_st = []
cam13_sorted_st = []
cam14_sorted_st = []
cam15_sorted_st = []
cam17_sorted_st = []
cam18_sorted_st = []
cam19_sorted_st = []
cam20_sorted_st = []
cam21_sorted_st = []
cam22_sorted_st = []
print("_______________________")
for i in range(0, len(sorted_corrected_ST)):
    if sorted_corrected_ST[i][0] == 1:
        cam1_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 2:
        cam2_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 11:
        cam11_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 12:
        cam12_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 13:
        cam13_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 14:
        cam14_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 15:
        cam15_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 17:
        cam17_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 18:
        cam18_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 19:
        cam19_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 20:
        cam20_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 21:
        cam21_sorted_st.append(sorted_corrected_ST[i])
    if sorted_corrected_ST[i][0] == 22:
        cam22_sorted_st.append(sorted_corrected_ST[i])



entry_sorted_cam2 = sorted(cam2_sorted_st, key=lambda l: (l[2],l[3]), reverse=False)

intervals1 = []
print(cam1_sorted_st)
for i in range(0, len(cam1_sorted_st)):
    if cam1_sorted_st[i][7] == 1:
        exit_min = cam1_sorted_st[i][4]
        exit_sec = cam1_sorted_st[i][5]

        diff = (exit_min - 27, exit_sec)

        intervals1.append(diff)

print(intervals1)


intervals2 = []
print(entry_sorted_cam2)
for i in range(0, len(entry_sorted_cam2)):
    if entry_sorted_cam2[i][6] == 1:
        entry_min = entry_sorted_cam2[i][2]
        entry_sec = entry_sorted_cam2[i][3]

        diff = (entry_min - 27, entry_sec)

        intervals2.append(diff)

print(intervals2)