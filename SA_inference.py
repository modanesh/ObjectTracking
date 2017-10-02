import re
from math import floor
from random import randint
from image_handler import hue_from_rgb
from image_handler import hue_from_image


def evaluator(assignment_array):
    # barresi monaseb budane assignment ha:
    #   - fasele rangi (color threshold)
    #   - fasele zamani (time threshold)
    #   - ehtemale harekat beine mabda va maghsad

    evaluations = []
    for i in range(0, len(assignment_array)):
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

        color_prob_1 = round(1 - round(hue_diff/360, 2), 2)
        color_prob_2 = round(1 - round(de_diff/100, 2), 2)



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



        time_prob_1 = round(1 - round(diff_in_seconds/70, 2), 2)

        time_diff = 0

        file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_time_differences.txt")
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

        file = open("/Users/Mohamad/Desktop/MulticameraObjectDetection/OurCode/ObjectTracking/txt_files/all_in_out_probabilities.txt")
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

        path_prob = round(prob_in*prob_out/10000, 2)

        evaluations.append((color_prob_1, color_prob_2, time_prob_1, time_prob_2, path_prob))
    return evaluations


def do_assignments(subproblem):
    OT = []
    IT = []
    assignments = []
    evaluation = []
    for i in range(0, len(subproblem)):
        if i < floor(len(subproblem)/2):
            OT.append(subproblem[i])
        else:
            IT.append(subproblem[i])

    if len(subproblem) > 2:
        for i in range(0, len(OT)):
            assignments.append((OT[i], IT[i]))

    else:
        assignments.append((subproblem[0], subproblem[1]))

    print(assignments)

    evaluation = evaluator(assignments)
    


    return evaluation


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
            print(probs)

    return probs

if __name__ == '__main__':
    probabilities = starting_step()
