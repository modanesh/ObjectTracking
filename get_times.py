import os
import re

import math



def extract_frame_time():
    for camera in cameras_fps_times:
        for filename in os.listdir("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/"+str(camera[0])+"/better_cropped_frames/"):
            if filename.endswith("jpg"):
                id = [int(s) for s in re.findall(r'\d+', filename)][0]
                frame = [int(s) for s in re.findall(r'\d+', filename)][1]

                seconds = math.floor(frame/camera[1])

                minute = math.floor(seconds/60)
                second = seconds - (minute * 60)

                start_hour = int(str(camera[2])[0:2])
                start_min = int(str(camera[2])[2:4])
                start_sec = int(str(camera[2])[4:6])

                new_min = start_min + minute
                if start_sec + second > 60:
                    new_sec = (start_sec + second) % 60
                    new_min += 1
                else:
                    new_sec = start_sec + second


                file.write("%d \t" % camera[0])
                file.write("%d \t" % id)
                file.write("%d%d%d \n" % (start_hour, new_min, new_sec))

    file.close()



def extract_inout_time(index):
    camera_info = cameras_fps_times[index-1]
    ann_file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/resources/"+str(index)+".txt")
    id_times = []
    frames = []
    times = []
    start_end_times = []
    for line in ann_file.readlines():
        if line.startswith("101"):

            id = [int(s) for s in re.findall(r'\d+', line)][1]
            frame_number = [int(s) for s in re.findall(r'\d+', line)][7]
            exists = [int(s) for s in re.findall(r'\d+', line)][8]

            if id == 1 and exists == 1:
                frames.append(frame_number)

                seconds = math.floor(frame_number / camera_info[1])

                minute = math.floor(seconds / 60)
                second = seconds - (minute * 60)

                start_hour = int(str(camera_info[2])[0:2])
                start_min = int(str(camera_info[2])[2:4])
                start_sec = int(str(camera_info[2])[4:6])

                new_min = start_min + minute
                if start_sec + second > 60:
                    new_sec = (start_sec + second) % 60
                    new_min += 1
                else:
                    new_sec = start_sec + second





                times.append((id, frame_number, start_hour, new_min, new_sec))

    print(times)
    print(times[0])
    print(times[-1])
    start_end_times.append(times[0])
    start_end_times.append(times[-1])
    print(start_end_times)








if __name__ == '__main__':
    file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt", "w")
    cameras_fps_times = [(1, 18, 122725), (2, 25, 122700), (11, 18, 122725), (12, 25, 122700), (13, 25, 122700),
                         (14, 25, 122700), (15, 18, 122725), (17, 25, 122700), (18, 25, 122700), (19, 25, 122700),
                         (20, 25, 122700), (21, 18, 122725), (22, 25, 122700)]

    extract_frame_time()
    index = 1
    extract_inout_time(index)