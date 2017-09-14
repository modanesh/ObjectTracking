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


def subproblem_generator(ag, sct):
    it = []
    ot = []
    s = []

    for i in range(0, len(sct)):
        for j in range(0, len(sct)):
            if sct[i][5] == sct[j][4]:
                s.append((sct[i][1], sct[i][2], sct[i][3], sct[i][4], sct[i][5], sct[j][1], sct[j][2], sct[j][3], sct[j][4], sct[j][5]))

