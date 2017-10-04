import re
from math import floor
from random import randint
import random
import itertools
from image_handler import hue_from_rgb
from image_handler import hue_from_image


def l1_evaluator(assignment_array):
    # barresi monaseb budane assignment ha:
    #   - fasele rangi (color threshold)
    #   - fasele zamani (time threshold)
    #   - ehtemale harekat beine mabda va maghsad

    evaluations = []

    # Get color differences
    # if hue_diff and de_diff are 0, they don't have colors. so the color differences cannot be used.
    cam_1 = assignment_array[0][1]
    id_1 = assignment_array[0][2]
    cam_2 = assignment_array[1][1]
    id_2 = assignment_array[1][2]
    hue_diff = 360
    de_diff = 100

    file = open(
        "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_color_differences.txt")
    for line in file.readlines():
        if line.startswith("(("):
            cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
            id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
            cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
            id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
            hue_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
            de_diff_file = [int(s) for s in re.findall(r'\d+', line)][5]
            if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
                hue_diff = hue_diff_file
                de_diff = de_diff_file

    color_prob_1 = round(1 - round(hue_diff / 360, 2), 2)
    color_prob_2 = round(1 - round(de_diff / 100, 2), 2)

    # Get time differences
    # first, use entry exit time differences. second, use the time differences of captured frames(from excel).
    # if time_diff is 0, there is no captured frame, so the second time difference cannot be used.
    min_1 = assignment_array[0][3]
    sec_1 = assignment_array[0][4]
    min_2 = assignment_array[1][3]
    sec_2 = assignment_array[1][4]

    if min_2 > min_1 and sec_2 > sec_1:
        diff_in_seconds = 60 * (min_2 - min_1) + (sec_2 - sec_1)
    elif min_2 == min_1 + 1 and sec_2 < sec_1:
        diff_in_seconds = sec_2 + 60 - sec_1
    elif min_2 == min_1 + 2 and sec_2 < sec_1:
        diff_in_seconds = 60 + sec_2 + 60 - sec_1
    elif min_2 == min_1 and sec_2 > sec_1:
        diff_in_seconds = sec_2 - sec_1
    elif min_2 == min_1 and sec_2 == sec_1:
        diff_in_seconds = 0
    else:
        diff_in_seconds = 1

    time_prob_1 = round(1 - round(diff_in_seconds / 70, 2), 2)

    time_diff = 0

    file = open(
        "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
    for line in file.readlines():
        if line.startswith("(("):
            cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
            id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
            cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
            id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
            time_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
            if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
                time_diff = time_diff_file

    if time_diff < 50:
        time_prob_2 = 0.75
    else:
        time_prob_2 = 0.25

    # Calculate the probability of moving between source and destination.
    x_1_in = assignment_array[0][5]
    x_1_out = assignment_array[0][6]
    x_2_in = assignment_array[1][5]
    x_2_out = assignment_array[1][6]

    prob_in = 0
    prob_out = 0

    file = open(
        "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
    for line in file.readlines():
        if line.startswith("("):
            cam_file = [int(s) for s in re.findall(r'\d+', line)][0]
            x_file = [int(s) for s in re.findall(r'\d+', line)][1]
            prob_file = [int(s) for s in re.findall(r'\d+', line)][2]
            inout_file = [int(s) for s in re.findall(r'\d+', line)][3]

            if cam_file == cam_1 and x_1_out == x_file and inout_file == 1:
                prob_out = prob_file

            if cam_file == cam_2 and x_2_in == x_file and inout_file == 0:
                prob_in = prob_file

    path_prob = round(prob_in * prob_out / 10000, 2)

    evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
    return evaluations


def evaluator(assignment_array, counter):
    # barresi monaseb budane assignment ha:
    #   - fasele rangi (color threshold)
    #   - fasele zamani (time threshold)
    #   - ehtemale harekat beine mabda va maghsad

    evaluations = []

    for i in range(0, counter):
        # Get color differences
        # if hue_diff and de_diff are 0, they don't have colors. so the color differences cannot be used.
        cam_1 = assignment_array[i][0][1]
        id_1 = assignment_array[i][0][2]
        cam_2 = assignment_array[i][1][1]
        id_2 = assignment_array[i][1][2]
        hue_diff = 360
        de_diff = 100

        file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_color_differences.txt")
        for line in file.readlines():
            if line.startswith("(("):
                cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
                id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
                cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
                id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
                hue_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
                de_diff_file = [int(s) for s in re.findall(r'\d+', line)][5]
                if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
                    hue_diff = hue_diff_file
                    de_diff = de_diff_file

        color_prob_1 = round(1 - round(hue_diff / 360, 2), 2)
        color_prob_2 = round(1 - round(de_diff / 100, 2), 2)

        # Get time differences
        # first, use entry exit time differences. second, use the time differences of captured frames(from excel).
        # if time_diff is 0, there is no captured frame, so the second time difference cannot be used.
        min_1 = assignment_array[i][0][3]
        sec_1 = assignment_array[i][0][4]
        min_2 = assignment_array[i][1][3]
        sec_2 = assignment_array[i][1][4]

        if min_2 > min_1 and sec_2 > sec_1:
            diff_in_seconds = 60 * (min_2 - min_1) + (sec_2 - sec_1)
        elif min_2 == min_1 + 1 and sec_2 < sec_1:
            diff_in_seconds = sec_2 + 60 - sec_1
        elif min_2 == min_1 + 2 and sec_2 < sec_1:
            diff_in_seconds = 60 + sec_2 + 60 - sec_1
        elif min_2 == min_1 and sec_2 > sec_1:
            diff_in_seconds = sec_2 - sec_1
        elif min_2 == min_1 and sec_2 == sec_1:
            diff_in_seconds = 0
        else:
            diff_in_seconds = 1

        time_prob_1 = round(1 - round(diff_in_seconds / 70, 2), 2)

        time_diff = 0

        file = open(
            "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
        for line in file.readlines():
            if line.startswith("(("):
                cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
                id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
                cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
                id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
                time_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
                if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
                    time_diff = time_diff_file

        if time_diff < 50:
            time_prob_2 = 0.75
        else:
            time_prob_2 = 0.25

        # Calculate the probability of moving between source and destination.
        x_1_in = assignment_array[i][0][5]
        x_1_out = assignment_array[i][0][6]
        x_2_in = assignment_array[i][1][5]
        x_2_out = assignment_array[i][1][6]

        prob_in = 0
        prob_out = 0

        file = open(
            "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
        for line in file.readlines():
            if line.startswith("("):
                cam_file = [int(s) for s in re.findall(r'\d+', line)][0]
                x_file = [int(s) for s in re.findall(r'\d+', line)][1]
                prob_file = [int(s) for s in re.findall(r'\d+', line)][2]
                inout_file = [int(s) for s in re.findall(r'\d+', line)][3]

                if cam_file == cam_1 and x_1_out == x_file and inout_file == 1:
                    prob_out = prob_file

                if cam_file == cam_2 and x_2_in == x_file and inout_file == 0:
                    prob_in = prob_file

        path_prob = round(prob_in * prob_out / 10000, 2)

        evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
    return evaluations


# def l3_evaluator(assignment_array):
#     # barresi monaseb budane assignment ha:
#     #   - fasele rangi (color threshold)
#     #   - fasele zamani (time threshold)
#     #   - ehtemale harekat beine mabda va maghsad
#
#     evaluations = []
#
#     for i in range(0, 3):
#         # Get color differences
#         # if hue_diff and de_diff are 0, they don't have colors. so the color differences cannot be used.
#         cam_1 = assignment_array[i][0][1]
#         id_1 = assignment_array[i][0][2]
#         cam_2 = assignment_array[i][1][1]
#         id_2 = assignment_array[i][1][2]
#         hue_diff = 360
#         de_diff = 100
#
#         file = open(
#             "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_color_differences.txt")
#         for line in file.readlines():
#             if line.startswith("(("):
#                 cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#                 id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#                 cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#                 id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#                 hue_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#                 de_diff_file = [int(s) for s in re.findall(r'\d+', line)][5]
#                 if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                     hue_diff = hue_diff_file
#                     de_diff = de_diff_file
#
#         color_prob_1 = round(1 - round(hue_diff / 360, 2), 2)
#         color_prob_2 = round(1 - round(de_diff / 100, 2), 2)
#
#         # Get time differences
#         # first, use entry exit time differences. second, use the time differences of captured frames(from excel).
#         # if time_diff is 0, there is no captured frame, so the second time difference cannot be used.
#         min_1 = assignment_array[i][0][3]
#         sec_1 = assignment_array[i][0][4]
#         min_2 = assignment_array[i][1][3]
#         sec_2 = assignment_array[i][1][4]
#
#         if min_2 > min_1 and sec_2 > sec_1:
#             diff_in_seconds = 60 * (min_2 - min_1) + (sec_2 - sec_1)
#         elif min_2 == min_1 + 1 and sec_2 < sec_1:
#             diff_in_seconds = sec_2 + 60 - sec_1
#         elif min_2 == min_1 + 2 and sec_2 < sec_1:
#             diff_in_seconds = 60 + sec_2 + 60 - sec_1
#         elif min_2 == min_1 and sec_2 > sec_1:
#             diff_in_seconds = sec_2 - sec_1
#         elif min_2 == min_1 and sec_2 == sec_1:
#             diff_in_seconds = 0
#         else:
#             diff_in_seconds = 1
#
#         time_prob_1 = round(1 - round(diff_in_seconds / 70, 2), 2)
#
#         time_diff = 0
#
#         file = open(
#             "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
#         for line in file.readlines():
#             if line.startswith("(("):
#                 cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#                 id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#                 cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#                 id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#                 time_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#                 if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                     time_diff = time_diff_file
#
#         if time_diff < 50:
#             time_prob_2 = 0.75
#         else:
#             time_prob_2 = 0.25
#
#         # Calculate the probability of moving between source and destination.
#         x_1_in = assignment_array[i][0][5]
#         x_1_out = assignment_array[i][0][6]
#         x_2_in = assignment_array[i][1][5]
#         x_2_out = assignment_array[i][1][6]
#
#         prob_in = 0
#         prob_out = 0
#
#         file = open(
#             "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
#         for line in file.readlines():
#             if line.startswith("("):
#                 cam_file = [int(s) for s in re.findall(r'\d+', line)][0]
#                 x_file = [int(s) for s in re.findall(r'\d+', line)][1]
#                 prob_file = [int(s) for s in re.findall(r'\d+', line)][2]
#                 inout_file = [int(s) for s in re.findall(r'\d+', line)][3]
#
#                 if cam_file == cam_1 and x_1_out == x_file and inout_file == 1:
#                     prob_out = prob_file
#
#                 if cam_file == cam_2 and x_2_in == x_file and inout_file == 0:
#                     prob_in = prob_file
#
#         path_prob = round(prob_in * prob_out / 10000, 2)
#
#         evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
#     return evaluations
#
#
# def l4_evaluator(assignment_array):
#     # barresi monaseb budane assignment ha:
#     #   - fasele rangi (color threshold)
#     #   - fasele zamani (time threshold)
#     #   - ehtemale harekat beine mabda va maghsad
#
#     evaluations = []
#
#     # Get color differences
#     # if hue_diff and de_diff are 0, they don't have colors. so the color differences cannot be used.
#     cam_1 = assignment_array[0][1]
#     id_1 = assignment_array[0][2]
#     cam_2 = assignment_array[1][1]
#     id_2 = assignment_array[1][2]
#     hue_diff = 360
#     de_diff = 100
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_color_differences.txt")
#     for line in file.readlines():
#         if line.startswith("(("):
#             cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#             hue_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#             de_diff_file = [int(s) for s in re.findall(r'\d+', line)][5]
#             if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                 hue_diff = hue_diff_file
#                 de_diff = de_diff_file
#
#     color_prob_1 = round(1 - round(hue_diff / 360, 2), 2)
#     color_prob_2 = round(1 - round(de_diff / 100, 2), 2)
#
#     # Get time differences
#     # first, use entry exit time differences. second, use the time differences of captured frames(from excel).
#     # if time_diff is 0, there is no captured frame, so the second time difference cannot be used.
#     min_1 = assignment_array[0][3]
#     sec_1 = assignment_array[0][4]
#     min_2 = assignment_array[1][3]
#     sec_2 = assignment_array[1][4]
#
#     if min_2 > min_1 and sec_2 > sec_1:
#         diff_in_seconds = 60 * (min_2 - min_1) + (sec_2 - sec_1)
#     elif min_2 == min_1 + 1 and sec_2 < sec_1:
#         diff_in_seconds = sec_2 + 60 - sec_1
#     elif min_2 == min_1 + 2 and sec_2 < sec_1:
#         diff_in_seconds = 60 + sec_2 + 60 - sec_1
#     elif min_2 == min_1 and sec_2 > sec_1:
#         diff_in_seconds = sec_2 - sec_1
#     elif min_2 == min_1 and sec_2 == sec_1:
#         diff_in_seconds = 0
#     else:
#         diff_in_seconds = 1
#
#     time_prob_1 = round(1 - round(diff_in_seconds / 70, 2), 2)
#
#     time_diff = 0
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
#     for line in file.readlines():
#         if line.startswith("(("):
#             cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#             time_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#             if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                 time_diff = time_diff_file
#
#     if time_diff < 50:
#         time_prob_2 = 0.75
#     else:
#         time_prob_2 = 0.25
#
#     # Calculate the probability of moving between source and destination.
#     x_1_in = assignment_array[0][5]
#     x_1_out = assignment_array[0][6]
#     x_2_in = assignment_array[1][5]
#     x_2_out = assignment_array[1][6]
#
#     prob_in = 0
#     prob_out = 0
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
#     for line in file.readlines():
#         if line.startswith("("):
#             cam_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             x_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             prob_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             inout_file = [int(s) for s in re.findall(r'\d+', line)][3]
#
#             if cam_file == cam_1 and x_1_out == x_file and inout_file == 1:
#                 prob_out = prob_file
#
#             if cam_file == cam_2 and x_2_in == x_file and inout_file == 0:
#                 prob_in = prob_file
#
#     path_prob = round(prob_in * prob_out / 10000, 2)
#
#     evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
#     return evaluations


# def l5_evaluator(assignment_array):
#     # barresi monaseb budane assignment ha:
#     #   - fasele rangi (color threshold)
#     #   - fasele zamani (time threshold)
#     #   - ehtemale harekat beine mabda va maghsad
#
#     evaluations = []
#
#     # Get color differences
#     # if hue_diff and de_diff are 0, they don't have colors. so the color differences cannot be used.
#     cam_1 = assignment_array[0][1]
#     id_1 = assignment_array[0][2]
#     cam_2 = assignment_array[1][1]
#     id_2 = assignment_array[1][2]
#     hue_diff = 360
#     de_diff = 100
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_color_differences.txt")
#     for line in file.readlines():
#         if line.startswith("(("):
#             cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#             hue_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#             de_diff_file = [int(s) for s in re.findall(r'\d+', line)][5]
#             if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                 hue_diff = hue_diff_file
#                 de_diff = de_diff_file
#
#     color_prob_1 = round(1 - round(hue_diff / 360, 2), 2)
#     color_prob_2 = round(1 - round(de_diff / 100, 2), 2)
#
#     # Get time differences
#     # first, use entry exit time differences. second, use the time differences of captured frames(from excel).
#     # if time_diff is 0, there is no captured frame, so the second time difference cannot be used.
#     min_1 = assignment_array[0][3]
#     sec_1 = assignment_array[0][4]
#     min_2 = assignment_array[1][3]
#     sec_2 = assignment_array[1][4]
#
#     if min_2 > min_1 and sec_2 > sec_1:
#         diff_in_seconds = 60 * (min_2 - min_1) + (sec_2 - sec_1)
#     elif min_2 == min_1 + 1 and sec_2 < sec_1:
#         diff_in_seconds = sec_2 + 60 - sec_1
#     elif min_2 == min_1 + 2 and sec_2 < sec_1:
#         diff_in_seconds = 60 + sec_2 + 60 - sec_1
#     elif min_2 == min_1 and sec_2 > sec_1:
#         diff_in_seconds = sec_2 - sec_1
#     elif min_2 == min_1 and sec_2 == sec_1:
#         diff_in_seconds = 0
#     else:
#         diff_in_seconds = 1
#
#     time_prob_1 = round(1 - round(diff_in_seconds / 70, 2), 2)
#
#     time_diff = 0
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
#     for line in file.readlines():
#         if line.startswith("(("):
#             cam_1_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             id_1_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             cam_2_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             id_2_file = [int(s) for s in re.findall(r'\d+', line)][3]
#             time_diff_file = [int(s) for s in re.findall(r'\d+', line)][4]
#             if cam_1 == cam_1_file and id_1 == id_1_file and cam_2 == cam_2_file and id_2 == id_2_file:
#                 time_diff = time_diff_file
#
#     if time_diff < 50:
#         time_prob_2 = 0.75
#     else:
#         time_prob_2 = 0.25
#
#     # Calculate the probability of moving between source and destination.
#     x_1_in = assignment_array[0][5]
#     x_1_out = assignment_array[0][6]
#     x_2_in = assignment_array[1][5]
#     x_2_out = assignment_array[1][6]
#
#     prob_in = 0
#     prob_out = 0
#
#     file = open(
#         "/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
#     for line in file.readlines():
#         if line.startswith("("):
#             cam_file = [int(s) for s in re.findall(r'\d+', line)][0]
#             x_file = [int(s) for s in re.findall(r'\d+', line)][1]
#             prob_file = [int(s) for s in re.findall(r'\d+', line)][2]
#             inout_file = [int(s) for s in re.findall(r'\d+', line)][3]
#
#             if cam_file == cam_1 and x_1_out == x_file and inout_file == 1:
#                 prob_out = prob_file
#
#             if cam_file == cam_2 and x_2_in == x_file and inout_file == 0:
#                 prob_in = prob_file
#
#     path_prob = round(prob_in * prob_out / 10000, 2)
#
#     evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
#     return evaluations


def evaluator_manager(assignment_array):
    if len(assignment_array) == 2:
        return evaluator(assignment_array, 2)
    elif len(assignment_array) == 3:
        return evaluator(assignment_array, 3)
    elif len(assignment_array) == 4:
        return evaluator(assignment_array, 4)
    elif len(assignment_array) == 5:
        return evaluator(assignment_array, 5)


def do_assignments(subproblem):
    evaluations = []
    assignments = []
    final_assignments = []

    combinations = list(itertools.combinations(subproblem, 2))

    if len(subproblem) == 2:
        assignments = combinations
    else:
        assignments = list(itertools.combinations(combinations, int(len(subproblem)/2)))

    if len(assignments) == 1:
        final_assignments = assignments
    elif len(assignments) == 15:
        for i in range(0, len(assignments)):
            if assignments[i][0][0][1] != assignments[i][0][1][1]:
                if assignments[i][1][0][1] != assignments[i][1][1][1]:
                    if assignments[i][0][0][2] != assignments[i][1][0][2] and assignments[i][0][0][1] == assignments[i][1][0][1]:
                        if assignments[i][0][1][2] != assignments[i][1][1][2] and assignments[i][0][1][1] == assignments[i][1][1][1]:
                            final_assignments.append(assignments[i])
    elif len(assignments) == 455:
        for i in range(0, len(assignments)):
            if assignments[i][0][0][1] != assignments[i][0][1][1]:
                if assignments[i][1][0][1] != assignments[i][1][1][1]:
                    if assignments[i][2][0][1] != assignments[i][2][1][1]:
                        if assignments[i][0][0][2] != assignments[i][1][0][2] and assignments[i][0][0][1] == assignments[i][1][0][1]:
                            if assignments[i][0][1][2] != assignments[i][1][1][2] and assignments[i][0][1][1] == assignments[i][1][1][1]:
                                if assignments[i][0][0][2] != assignments[i][2][0][2] and assignments[i][0][0][1] == assignments[i][2][0][1]:
                                    if assignments[i][0][1][2] != assignments[i][2][1][2] and assignments[i][0][1][1] == assignments[i][2][1][1]:
                                        if assignments[i][2][0][2] != assignments[i][1][0][2] and assignments[i][2][0][1] == assignments[i][1][0][1]:
                                            if assignments[i][2][1][2] != assignments[i][1][1][2] and assignments[i][2][1][1] == assignments[i][1][1][1]:
                                                final_assignments.append(assignments[i])
    elif len(assignments) == 20475:
        for i in range(0, len(assignments)):
            if assignments[i][0][0][1] != assignments[i][0][1][1]:
                if assignments[i][1][0][1] != assignments[i][1][1][1]:
                    if assignments[i][2][0][1] != assignments[i][2][1][1]:
                        if assignments[i][3][0][1] != assignments[i][3][1][1]:
                            if assignments[i][0][0][2] != assignments[i][1][0][2] and assignments[i][0][0][1] == assignments[i][1][0][1]:
                                if assignments[i][0][1][2] != assignments[i][1][1][2] and assignments[i][0][1][1] == assignments[i][1][1][1]:
                                    if assignments[i][0][0][2] != assignments[i][2][0][2] and assignments[i][0][0][1] == assignments[i][2][0][1]:
                                        if assignments[i][0][1][2] != assignments[i][2][1][2] and assignments[i][0][1][1] == assignments[i][2][1][1]:
                                            if assignments[i][1][0][2] != assignments[i][2][0][2] and assignments[i][1][0][1] == assignments[i][2][0][1]:
                                                if assignments[i][1][1][2] != assignments[i][2][1][2] and assignments[i][1][1][1] == assignments[i][2][1][1]:
                                                    if assignments[i][0][0][2] != assignments[i][3][0][2] and assignments[i][0][0][1] == assignments[i][3][0][1]:
                                                        if assignments[i][0][1][2] != assignments[i][3][1][2] and assignments[i][0][1][1] == assignments[i][3][1][1]:
                                                            if assignments[i][1][0][2] != assignments[i][3][0][2] and assignments[i][1][0][1] == assignments[i][3][0][1]:
                                                                if assignments[i][1][1][2] != assignments[i][3][1][2] and assignments[i][1][1][1] == assignments[i][3][1][1]:
                                                                    if assignments[i][2][0][2] != assignments[i][3][0][2] and assignments[i][2][0][1] == assignments[i][3][0][1]:
                                                                        if assignments[i][2][1][2] != assignments[i][3][1][2] and assignments[i][2][1][1] == assignments[i][3][1][1]:
                                                                            final_assignments.append(assignments[i])
    elif len(assignments) == 1221759:
        for i in range(0, len(assignments)):
            if assignments[i][0][0][1] != assignments[i][0][1][1]:
                if assignments[i][1][0][1] != assignments[i][1][1][1]:
                    if assignments[i][2][0][1] != assignments[i][2][1][1]:
                        if assignments[i][3][0][1] != assignments[i][3][1][1]:
                            if assignments[i][4][0][1] != assignments[i][4][1][1]:
                                if assignments[i][0][0][2] != assignments[i][1][0][2] and assignments[i][0][0][1] == assignments[i][1][0][1]:
                                    if assignments[i][0][1][2] != assignments[i][1][1][2] and assignments[i][0][1][1] == assignments[i][1][1][1]:
                                        if assignments[i][0][0][2] != assignments[i][2][0][2] and assignments[i][0][0][1] == assignments[i][2][0][1]:
                                            if assignments[i][0][1][2] != assignments[i][2][1][2] and assignments[i][0][1][1] == assignments[i][2][1][1]:
                                                if assignments[i][1][0][2] != assignments[i][2][0][2] and assignments[i][1][0][1] == assignments[i][2][0][1]:
                                                    if assignments[i][1][1][2] != assignments[i][2][1][2] and assignments[i][1][1][1] == assignments[i][2][1][1]:
                                                        if assignments[i][0][0][2] != assignments[i][3][0][2] and assignments[i][0][0][1] == assignments[i][3][0][1]:
                                                            if assignments[i][0][1][2] != assignments[i][3][1][2] and assignments[i][0][1][1] == assignments[i][3][1][1]:
                                                                if assignments[i][1][0][2] != assignments[i][3][0][2] and assignments[i][1][0][1] == assignments[i][3][0][1]:
                                                                    if assignments[i][1][1][2] != assignments[i][3][1][2] and assignments[i][1][1][1] == assignments[i][3][1][1]:
                                                                        if assignments[i][2][0][2] != assignments[i][3][0][2] and assignments[i][2][0][1] == assignments[i][3][0][1]:
                                                                            if assignments[i][2][1][2] != assignments[i][3][1][2] and assignments[i][2][1][1] == assignments[i][3][1][1]:
                                                                                if assignments[i][0][0][2] != assignments[i][4][0][2] and assignments[i][0][0][1] == assignments[i][4][0][1]:
                                                                                    if assignments[i][0][1][2] != assignments[i][4][1][2] and assignments[i][0][1][1] == assignments[i][4][1][1]:
                                                                                        if assignments[i][1][0][2] != assignments[i][4][0][2] and assignments[i][1][0][1] == assignments[i][4][0][1]:
                                                                                            if assignments[i][1][1][2] != assignments[i][4][1][2] and assignments[i][1][1][1] == assignments[i][4][1][1]:
                                                                                                if assignments[i][2][0][2] != assignments[i][4][0][2] and assignments[i][2][0][1] == assignments[i][4][0][1]:
                                                                                                    if assignments[i][2][1][2] != assignments[i][4][1][2] and assignments[i][2][1][1] == assignments[i][4][1][1]:
                                                                                                        if assignments[i][3][0][2] != assignments[i][4][0][2] and assignments[i][3][0][1] == assignments[i][4][0][1]:
                                                                                                            if assignments[i][3][1][2] != assignments[i][4][1][2] and assignments[i][3][1][1] == assignments[i][4][1][1]:
                                                                                                                final_assignments.append(assignments[i])


    for i in range(0, len(final_assignments)):
        print("final_assignments[i]")
        print(len(final_assignments[i]))
        if len(final_assignments) == 1 and len(final_assignments[i]) == 2:
            evaluations.append(l1_evaluator(final_assignments[i]))
        else:

            evaluations.append(evaluator_manager(final_assignments[i]))

    print("evaluations")
    print(evaluations)


    # simulated_annealing(assignments, evaluations)



def simulated_annealing(assignments, evaluations):
    print("sa")
    print(assignments)
    print(evaluations)
    current_state = []
    # for i in range(0, len(evaluations)):








def starting_step():
    probs = []
    assignments = []

    # file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/subproblems.txt")
    file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/tmp.txt")
    for line in file.readlines():
        if line.startswith("(") and [int(s) for s in re.findall(r'\d+', line)][0] != 123:
            subproblem = []
            subproblem_number = len(line.split("(")) - 1
            for i in range(0, subproblem_number):
                sp_id = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 0]
                cam = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 1]
                id = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 2]
                min = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 3]
                sec = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 4]
                xin = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 5]
                xout = [int(s) for s in re.findall(r'\d+', line)][i * 7 + 6]

                subproblem.append((sp_id, cam, id, min, sec, xin, xout))

            probs = do_assignments(subproblem)
            # print(probs)

    return probs

if __name__ == '__main__':
    probabilities = starting_step()
