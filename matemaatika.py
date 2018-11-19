import copy
import math
import collections
from qm import QuineMcCluskey
from Taandatud import Taandatud as Ta

"""
A calculator for for Discreet Maths homework.185787.

Takes input (normal number system) and outputs all the steps and their results for the homework.
"""
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

while True:
    input_value = input("Please enter your ID: ")
    if not input_value.isdigit():
        print('Input value can not contain symbols or letters!')
    else:
        break

int_input = int(input_value)
print(f"Your ID's hex value is: {str(hex(int_input)).split('x')[1]}.")


def transform(int_in, max_length):
    counter = 0
    int_start = int_in
    length = len(hex(int_in)) - 2
    while length < max_length:
        counter += 1
        previous = int_in
        int_in = int_in * 7
        length = len(hex(int_in)) - 2
        print(f"{str(hex(previous)).split('x')[1]} -> {str(hex(int_in)).split('x')[1]}")

    print(f"{str(hex(int_start)).split('x')[1]} -> {str(hex(int_in)).split('x')[1]} "
          f"after multiplying with 7 {counter} times.")

    return int_in


int_input = transform(int_input, 7)


def ranges(int_in):
    value1 = []
    for char in hex(int_in).split('x')[1]:
        value1.append(int(char, 16))
    value2 = set(value1)
    return value1, value2


value_1_1, value_1 = ranges(int_input)
print(f"From {str(hex(int_input)).split('x')[1]} we get {value_1_1} and after sorting it we get {value_1}.\n"
      "This is your 1-de (ühtede) 'piirkond'.\n")

int_input = transform(int_input, 9)


def compare(val1, val2):
    for value in val1:
        if value in val2:
            val2.remove(value)
    return val2


value_2_1, value_2 = ranges(int_input)
value_2_1 = compare(value_1, copy.deepcopy(value_2))
print(f"From {str(hex(int_input)).split('x')[1]} we get {value_2_1} and after sorting it we get {value_2}."
      f"After comparing it with {value_1} we get {value_2_1}.\n"
      "This is your 'määramatusepiirkond'.\n")

value_3 = list(range(0, 16))
value_3_1 = compare(value_1, copy.deepcopy(value_3))
value_3_2 = compare(value_2, value_3_1)
print(f"From removing  1-de (ühtede) 'piirkond' ({value_1}) and 'määramatusepiirkond' ({value_2_1}) from {value_3}, " ## 1 - disj 2 - määr 3 - konj
      f"we get {value_3_2}.\n"
      "This is your 0-de (nullide) 'piirkond'.\n")

print(f'Your function will look as follows: f(x1...x4) = Σ{value_1}₁ {value_2_1}_'.replace('{', '(').replace('}', ')'))
print(value_1)
print(value_2_1)
print(value_3)
values = []
table = '|x1|x2|x3|x4|->|f|\n'
for i in range(0, 16):
    s = '|'
    b = bin(i)[2:].zfill(4)
    for c in str(b):
        s += f'{c} | '
    if i in value_1:
        v = '1'
    elif i in value_2:
        v = '-'
    elif i in value_3_2:
        v = '0'
    values.append(v)
    s += f'->| {v}|\n'
    table += s

print(table)

print("Karnaugh table will look as follows \nfirst in collumn is x1, second in collumn is x2, "
      "first in top line is x3, second in top line is x4")
print("   |00 |01 |11 |10")
new_list = []
positional_differences = [0, 1, 3, 2]

for i in range(4):
    for j in range(4):
        appendable = values[positional_differences[i] * 4 + positional_differences[j]]
        new_list.append(appendable)
        string_of_karnaugh = ' | '.join(new_list[-4:])
    position = str(bin(positional_differences[i]))[2:]
    if len(position) == 1:
        position = "0" + position
    print(position + " | " + string_of_karnaugh)

horisontal_karnaugh_line = []
vertical_karnaugh_line = []
horisontal_karnaugh_index = [0 ,1 ,2 ,3]
generic_list = []

for j in range(4):
    for i in range(4):
        generic_list.append(new_list[horisontal_karnaugh_index[i] + 4 * j])
    horisontal_karnaugh_line.append(generic_list)
    generic_list = []

TaKNK = []
TKNK = []
MKNK = []
TaDNK = []
TDNK = []
MDNK = {}

range_of_ones = list(value_1).copy()
range_of_zeroes = value_3_2.copy()
range_of_uncertainty = list(value_2_1).copy()

qm = QuineMcCluskey()
MDNK = qm.simplify(range_of_ones, range_of_uncertainty)
MKNK = qm.simplify(range_of_zeroes, range_of_uncertainty)

index = ["0", "1"]
foo = []
poo = []
for elem in horisontal_karnaugh_line:
    for element in elem:
        if element == "-":
            poo.append("2")
        else:
            poo.append(element)
    foo.append(poo)
    poo = []
horisontal_karnaugh_line = foo


def checker(generic_list):
    all_answers = []
    for num, key in enumerate(dictionary):
        for i in range(len(dictionary[key])):
            result = all(int(elem) in dictionary[key][i].copy() for elem in generic_list.copy())
            all_answers.append(result)
    return not any(all_answers)


def _16_to_3(d2_list):
    correct_form = []
    for element in d2_list:
        appendable = qm.simplify(element, [16])
        correct_form.append(list(appendable)[0][1:])
    return correct_form


def _3_to_16(d2_list):
    correct_form = []
    will_go = False
    for value in d2_list:
        if "-" in value:
            will_go = True
    if will_go:
        for place, element in enumerate(d2_list):
            for i in range(4):
                if element[i] == "-":
                    proxy = d2_list.pop(place)
                    for binary in range(2):
                        d2_list.append(proxy[0:i] + str(binary) + proxy[i+1:])
                    return _3_to_16(d2_list)
    else:
        for element in d2_list:
            correct_form.append(eval("0b" + element))
        return set(correct_form)


def remove_error(correct, wrong):
    for element in wrong:
        for char in element:
            if char not in correct:
                wrong.remove(element)
                return remove_error(correct, wrong)
    return wrong


check_MDNK = _3_to_16(list(MDNK.copy()))
check_MKNK = _3_to_16(list(MKNK.copy()))

for turn in range(2):
    if turn == 0:
        for element in Ta(horisontal_karnaugh_line, turn).values():
            if element != []:
                for value in element:
                    TaDNK.append(value)

    elif turn == 1:
        for element in Ta(horisontal_karnaugh_line, turn).values():
            if element != []:
                for value in element:
                    TaKNK.append(value)

    karnaugh_index = [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]

    for i in range(4):
        for j in range(4):
            # 1x1
            if turn == 1:
                if karnaugh_index[i][j] in check_MDNK:
                    proxy = sorted([karnaugh_index[i][j]])
                    TDNK.append(sorted([karnaugh_index[i][j]]))
            if turn == 0:
                if karnaugh_index[i][j] in check_MKNK:
                    proxy = sorted([karnaugh_index[i][j]])
                    TKNK.append(sorted([karnaugh_index[i][j]]))

###remove error

TaDNK = remove_error(check_MDNK, TaDNK)
TaKNK = remove_error(check_MKNK, TaKNK)


TDNK = _16_to_3(TDNK)
TKNK = _16_to_3(TKNK)
TaDNK = _16_to_3(TaDNK)
TaKNK = _16_to_3(TaKNK)

print()
print("Taandatud DNK : ", TaDNK)
print("Täielik DNK : ", TDNK)
print("Minimaalne DNK : ", list(MDNK))
print()
print("Taandatud KNK : ", TaKNK)
print("Täielik KNK : ", TKNK)
print("Minimaalne KNK : ", list(MKNK))
print()
print()
print()
print()
