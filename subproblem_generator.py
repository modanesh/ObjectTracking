# single track for each person in each camera: tin, tout, xin, xout
import re


def read_ST_from_file():
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



def create_corrected_ST():
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



def dividing_corrected_ST_by_time():
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


def entry_exit_time_calculation():
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




if __name__ == '__main__':
    print("hi")