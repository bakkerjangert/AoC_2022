import time
from copy import deepcopy
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data


def print_dict_pt1():
    for i in range(1, no_rows + 1):
        print(crates_pt1[i])


def print_dict_pt2():
    for i in range(1, no_rows + 1):
        print(crates_pt2[i])

tic = time.perf_counter()
PRINT_STEPS = False
file = 'input.txt'
# file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()
layout, instructions, no_rows = [], [], None
for line in lines:
    if '[' in line:
        layout.append(line)
    if 'move' in line:
        instructions.append(line)
    if '   ' in line and '[' not in line:
        while line[-1] == ' ':
            line = line[:-1]
        no_rows = int(line.split(' ')[-1])

crates_pt1 = dict()
for i in range(1, no_rows + 1):
    crates_pt1[i] = []
for line in layout[::-1]:
    for i in range(no_rows):
        if len(line) > i * 4:
            if line[1 + i * 4] != ' ':
                crates_pt1[i + 1].append(line[1 + i * 4])

crates_pt2 = deepcopy(crates_pt1)

# Part 1
if PRINT_STEPS:
    print('Start configuration part 1')
    print_dict_pt1()
for line in instructions:
    number_of_crates = int(line.split(' ')[1])
    from_row = int(line.split(' ')[3])
    to_row = int(line.split(' ')[5])
    moved_crates = crates_pt1[from_row][-number_of_crates:]
    crates_pt1[from_row] = crates_pt1[from_row][:-number_of_crates]
    crates_pt1[to_row] = crates_pt1[to_row] + moved_crates[::-1]
    if PRINT_STEPS:
        print('\nAfter next move')
        print_dict_pt1()
print('\nThe answer to part 1:')
for i in range(1, no_rows + 1):
    print(crates_pt1[i][-1], end='')
print('')

# Part 2
if PRINT_STEPS:
    print('\nStart configuration part 2')
    print_dict_pt2()

for line in instructions:
    number_of_crates = int(line.split(' ')[1])
    from_row = int(line.split(' ')[3])
    to_row = int(line.split(' ')[5])
    moved_crates = crates_pt2[from_row][-number_of_crates:]
    crates_pt2[from_row] = crates_pt2[from_row][:-number_of_crates]
    crates_pt2[to_row] = crates_pt2[to_row] + moved_crates
    if PRINT_STEPS:
        print('\nAfter next move')
        print_dict_pt2()
print('\nThe answer to part 2:')
for i in range(1, no_rows + 1):
    print(crates_pt2[i][-1], end='')
print('')

toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
