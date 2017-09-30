# single track for each person in each camera: tin, tout, xin, xout
import re


def prepare_candidate_ST():
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


    intervals1 = []
    for i in range(0, len(cam11_sorted_st)):
        if cam11_sorted_st[i][6] == 2:
            exit_min = cam11_sorted_st[i][2]
            exit_sec = cam11_sorted_st[i][3]

            intervals1.append((cam11_sorted_st[i][0], cam11_sorted_st[i][1], exit_min - 27, exit_sec, cam11_sorted_st[i][6], cam11_sorted_st[i][7]))

    print(sorted(intervals1, key=lambda l: (l[2],l[3]), reverse=False))

    intervals2 = []
    for i in range(0, len(cam13_sorted_st)):
        if cam13_sorted_st[i][6] == 4:
            entry_min = cam13_sorted_st[i][2]
            entry_sec = cam13_sorted_st[i][3]

            intervals2.append((cam13_sorted_st[i][0], cam13_sorted_st[i][1], entry_min - 27, entry_sec, cam13_sorted_st[i][6], cam13_sorted_st[i][7]))

    print(sorted(intervals2, key=lambda l: (l[2],l[3]), reverse=False))

    intervals3 = []
    for i in range(0, len(cam21_sorted_st)):
        if cam21_sorted_st[i][6] == 3:
            entry_min = cam21_sorted_st[i][2]
            entry_sec = cam21_sorted_st[i][3]

            intervals3.append((cam21_sorted_st[i][0], cam21_sorted_st[i][1], entry_min - 27, entry_sec, cam21_sorted_st[i][6], cam21_sorted_st[i][7]))

    print(sorted(intervals3, key=lambda l: (l[2],l[3]), reverse=False))

    intervals5 = []
    for i in range(0, len(cam21_sorted_st)):
        if cam21_sorted_st[i][6] == 4:
            entry_min = cam21_sorted_st[i][2]
            entry_sec = cam21_sorted_st[i][3]

            intervals5.append((cam21_sorted_st[i][0], cam21_sorted_st[i][1], entry_min - 27, entry_sec, cam21_sorted_st[i][6], cam21_sorted_st[i][7]))

    print(sorted(intervals5, key=lambda l: (l[2],l[3]), reverse=False))

    intervals4 = []
    for i in range(0, len(cam22_sorted_st)):
        if cam22_sorted_st[i][7] == 1:
            entry_min = cam22_sorted_st[i][4]
            entry_sec = cam22_sorted_st[i][5]

            intervals4.append((cam22_sorted_st[i][0], cam22_sorted_st[i][1], entry_min - 27, entry_sec, cam22_sorted_st[i][6], cam22_sorted_st[i][7]))

    print(sorted(intervals4, key=lambda l: (l[2],l[3]), reverse=False))



def extract_subproblem():
    one_exit = [(1, 6, 0, 14, 2, 1), (1, 7, 0, 31, 2, 1), (1, 9, 0, 33, 2, 1), (1, 11, 0, 40, 2, 1), (1, 12, 0, 41, 2, 1), (1, 10, 0, 42, 2, 1), (1, 15, 0, 58, 2, 1), (1, 18, 1, 15, 2, 1), (1, 21, 1, 38, 2, 1), (1, 22, 1, 39, 2, 1), (1, 25, 1, 47, 1, 1), (1, 27, 1, 49, 1, 1), (1, 20, 1, 57, 2, 1), (1, 28, 1, 57, 2, 1), (1, 29, 2, 7, 1, 1), (1, 37, 2, 31, 2, 1), (1, 42, 2, 40, 2, 1), (1, 41, 2, 41, 2, 1), (1, 49, 3, 9, 2, 1), (1, 50, 3, 23, 2, 1), (1, 52, 3, 31, 2, 1), (1, 53, 3, 35, 2, 1), (1, 54, 3, 36, 2, 1), (1, 55, 3, 37, 2, 1), (1, 57, 3, 38, 2, 1), (1, 59, 3, 45, 2, 1), (1, 60, 3, 46, 2, 1), (1, 31, 3, 54, 1, 1), (1, 62, 3, 56, 2, 1), (1, 63, 3, 57, 1, 1), (1, 64, 4, 5, 2, 1), (1, 66, 4, 32, 2, 1), (1, 67, 4, 36, 2, 1), (1, 72, 4, 43, 2, 1), (1, 71, 4, 44, 2, 1)]
    two_enter = [(2, 11, 0, 15, 1, 3), (2, 16, 0, 32, 1, 3), (2, 17, 0, 34, 1, 3), (2, 18, 0, 40, 1, 3), (2, 19, 0, 42, 1, 3), (2, 20, 0, 43, 1, 4), (2, 25, 0, 59, 1, 3), (2, 28, 1, 17, 1, 4), (2, 36, 1, 40, 1, 4), (2, 37, 1, 40, 1, 4), (2, 39, 1, 49, 1, 1), (2, 40, 1, 50, 1, 1), (2, 41, 1, 58, 1, 3), (2, 42, 1, 59, 1, 1), (2, 48, 2, 10, 1, 3)]
    not_gaps = []
    for i in range(0, len(one_exit)-1):
        for j in range(0, len(two_enter)-1):
            if one_exit[i][2] == two_enter[j][2] and 0 < two_enter[j][3] - one_exit[i][3] < 5:
                print("___________________")
                print(one_exit[i])
                print(two_enter[j])



if __name__ == '__main__':
    print("I need help, from God!")
    extract_subproblem()