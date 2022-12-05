import time
from copy import deepcopy
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data

def print_dict_pt1():
    for i in range(1, no_rows + 1):
        print(crates[i])

def print_dict_pt2():
    for i in range(1, no_rows + 1):
        print(crates_pt2[i])

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()
no_rows = 9
crates = dict()
for i in range(1, no_rows + 1):
    crates[i] = []
layout = lines[0:8]
instructions = lines[10:]
for line in layout[::-1]:
    for i in range(9):
        if line[1 + i * 4] != ' ':
            crates[i + 1].append(line[1 + i * 4])

# Test values
# no_rows = 3
# crates = {1: ['Z', 'N'],
#           2: ['M', 'C', 'D'],
#           3: ['P']}
# instructions = ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']

crates_pt2 = deepcopy(crates)

# Part 1
# print('Start configuration part 1')
# print_dict()
for line in instructions:
    number_of_crates = int(line.split(' ')[1])
    from_row = int(line.split(' ')[3])
    to_row = int(line.split(' ')[5])
    moved_crates = crates[from_row][-number_of_crates:]
    crates[from_row] = crates[from_row][:-number_of_crates]
    crates[to_row] = crates[to_row] + moved_crates[::-1]
    # print('\nAfter next move')
    # print_dict()

for i in range(1, no_rows + 1):
    print(crates[i][-1], end='')
print('')

# Part 2
# print('Start configuration part 2')
# print_dict_pt2()

for line in instructions:
    number_of_crates = int(line.split(' ')[1])
    from_row = int(line.split(' ')[3])
    to_row = int(line.split(' ')[5])
    moved_crates = crates_pt2[from_row][-number_of_crates:]
    crates_pt2[from_row] = crates_pt2[from_row][:-number_of_crates]
    crates_pt2[to_row] = crates_pt2[to_row] + moved_crates
    # print('\nAfter next move')
    # print_dict_pt2()

for i in range(1, no_rows + 1):
    print(crates_pt2[i][-1], end='')
print('')

toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
