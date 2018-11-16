def checker(generic_list, dictionary):
    all_answers = []
    for num, key in enumerate(dictionary):
        for i in range(len(dictionary[key])):
            result = all(int(elem) in dictionary[key][i].copy() for elem in generic_list.copy())
            all_answers.append(result)
    return not any(all_answers)


def Taandatud(horisontal_karnaugh_line, turn):
    index = ["0", "1"]
    dictionary = {
        "_4x2": [],
        "_4x1": [],
        "_2x4": [],
        "_1x4": [],
        "_2x2": [],
        "_1x2": [],
        "_2x1": [],
        "_1x1": []
    }

    karnaugh_index = [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]

    for i in range(4):  # Taandatud DNK ja Taandatud KNK
        for j in range(4):
            # 4x2
            if horisontal_karnaugh_line[i][j] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i - 2][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 2][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i - 3][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 3][j - 1] != index[turn]:
                proxy = sorted([karnaugh_index[i][j],
                                karnaugh_index[i][j - 1],
                                karnaugh_index[i - 1][j],
                                karnaugh_index[i - 1][j - 1],
                                karnaugh_index[i - 2][j],
                                karnaugh_index[i - 2][j - 1],
                                karnaugh_index[i - 3][j],
                                karnaugh_index[i - 3][j - 1]])
                if checker(proxy, dictionary):
                    dictionary["_4x2"].append(proxy)
            # 2x4
            if horisontal_karnaugh_line[i][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 2] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j - 2] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 3] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j - 3] != index[turn]:
                proxy = sorted([karnaugh_index[i][j],
                                karnaugh_index[i][j - 1],
                                karnaugh_index[i][j - 2],
                                karnaugh_index[i][j - 3],
                                karnaugh_index[i - 1][j],
                                karnaugh_index[i - 1][j - 1],
                                karnaugh_index[i - 1][j - 2],
                                karnaugh_index[i - 1][j - 3]])
                if checker(proxy, dictionary):
                    dictionary["_2x4"].append(proxy)

    for i in range(4):
        for j in range(4):
            # 4x1
            if horisontal_karnaugh_line[i][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 2][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 3][j] != index[turn]:
                proxy = sorted([karnaugh_index[i][j], karnaugh_index[i - 1][j], karnaugh_index[i - 2][j],
                                karnaugh_index[i - 3][j]])
                if checker(proxy, dictionary):
                    dictionary["_4x1"].append(proxy)
            # 1x4
            if horisontal_karnaugh_line[i][j] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 2] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 3] != index[turn]:
                proxy = sorted([karnaugh_index[i][j], karnaugh_index[i][j - 1],
                                karnaugh_index[i][j - 2], karnaugh_index[i][j - 3]])
                if checker(proxy, dictionary):
                    dictionary["_2x4"].append(proxy)
            # 2x2
            if horisontal_karnaugh_line[i][j] != index[turn] and \
                    horisontal_karnaugh_line[i][j - 1] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j] != index[turn] and \
                    horisontal_karnaugh_line[i - 1][j - 1] != index[turn]:
                proxy = sorted([karnaugh_index[i][j], karnaugh_index[i][j - 1],
                                karnaugh_index[i - 1][j], karnaugh_index[i - 1][j - 1]])
                if checker(proxy, dictionary):
                    dictionary["_2x2"].append(proxy)

    for i in range(4):
        for j in range(4):
            # 2x1
            if horisontal_karnaugh_line[i][j] != index[turn] and horisontal_karnaugh_line[i - 1][j] != index[turn]:
                proxy = sorted([karnaugh_index[i][j], karnaugh_index[i - 1][j]])
                if checker(proxy, dictionary):
                    dictionary["_2x1"].append(sorted([karnaugh_index[i][j], karnaugh_index[i - 1][j]]))
            # 1x2
            if horisontal_karnaugh_line[i][j] != index[turn] and horisontal_karnaugh_line[i][j - 1] != index[turn]:
                proxy = sorted([karnaugh_index[i][j], karnaugh_index[i][j - 1]])
                if checker(proxy, dictionary):
                    dictionary["_1x2"].append(sorted([karnaugh_index[i][j], karnaugh_index[i][j - 1]]))

    return dictionary
