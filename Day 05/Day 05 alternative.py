import time
from copy import deepcopy
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data

tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'
# file = 'aoc_2022_day05_large_input.txt'
# file = 'aoc_2022_day05_large_input-2.txt'
# file = 'aoc_2022_day05_large_input-3.txt'

with open(file) as f:
    lines = f.read().splitlines()
no_stacks, max_height = 0, 0
for i, line in enumerate(lines):
    number = line.count('[')
    if number == 0:
        max_height = i
        break
    no_stacks = max(no_stacks, number)

stacks, instructions = dict(), []
for i in range(no_stacks):
    stacks[i + 1] = 0

for line in lines:
    if '[' in line:
        line = line + ' ' * (4 * no_stacks - len(line))
        for i in range(no_stacks):
            if line[1 + 4 * i] != ' ':
                stacks[i + 1] += 1
    if 'move' in line:
        instructions.append([int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])])

# for key in stacks.keys():
#     print(key, stacks[key])
# print(f'max stack height = {max_height}')

# Generate length ending stacks
for line in instructions:
    stacks[line[1]] -= line[0]
    stacks[line[2]] += line[0]

# for key in stacks.keys():
#     print(key, stacks[key])

packages_pt1 = []  # Track of stacks [stack, height]
for i in range(no_stacks):
    packages_pt1.append([i + 1, stacks[i + 1]])
packages_pt2 = deepcopy(packages_pt1)
# print(packages_pt2)
line_counter = 0
numbers_pt1 = list(range(1, no_stacks + 1))
numbers_pt2 = list(range(1, no_stacks + 1))
for line in instructions[::-1]:
    if line[2] in numbers_pt1:
        for i in range(no_stacks):
            if packages_pt1[i][0] == line[2]:
                if packages_pt1[i][1] > stacks[line[2]] - line[0]:
                    delta_1 = 1 + (stacks[packages_pt1[i][0]] - packages_pt1[i][1])
                    packages_pt1[i][0] = line[1]
                    packages_pt1[i][1] = stacks[line[1]] + delta_1
                    numbers_pt1.remove(line[2])
                    numbers_pt1.append(line[1])
    if line[2] in numbers_pt2:
        for i in range(no_stacks):
            if packages_pt2[i][0] == line[2]:
                if packages_pt2[i][1] > stacks[line[2]] - line[0]:
                    delta_2 = line[0] - (stacks[packages_pt2[i][0]] - packages_pt2[i][1])
                    packages_pt2[i][0] = line[1]
                    packages_pt2[i][1] = stacks[line[1]] + delta_2
                    numbers_pt2.remove(line[2])
                    numbers_pt2.append(line[1])
    # print(packages_pt2)
    stacks[line[2]] -= line[0]
    stacks[line[1]] += line[0]
    line_counter += 1
    if line_counter % 1000 == 0:
        print(f'Calculation at {round(line_counter / len(instructions) * 100,2)} %')

for package in packages_pt1:
    char = lines[max_height - package[1]][1 + 4 * (package[0] - 1)]
    print(char, end='')
print('')

for package in packages_pt2:
    char = lines[max_height - package[1]][1 + 4 * (package[0] - 1)]
    print(char, end='')
print('')

toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
