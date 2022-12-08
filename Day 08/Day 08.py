import time
import numpy as np
from copy import deepcopy
# Advent of Code 2022 - Day 08 part 1 & 2
# https://adventofcode.com/2022/day/8

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'

def count_trees(line):
    counter = np.zeros(len(line), dtype=int)
    len_start, len_end = -1, -1
    for i in range(len(line)):
        if line[i] > len_start:
            counter[i] = 1
            len_start = line[i]
        j = len(line) - 1 - i
        if line[j] > len_end:
            counter[j] = 1
            len_end = line[j]
    return counter


with open(file) as f:
    lines = f.read().splitlines()

trees = []
for line in lines:
    trees.append(list(map(int, list(line))))
trees = np.array(trees, dtype=int)
visible = np.zeros(trees.shape, dtype=int)
# print(trees)
for i in range(trees.shape[0]):
    row = trees[i]
    mask = count_trees(row)
    visible[i] = mask
for j in range(trees.shape[1]):
    col = trees[:, j]
    mask = count_trees(col)
    for i, tree in enumerate(mask):
        if tree == 1:
            visible[i, j] = 1

print(f'The answer to part 1 = {visible.sum()}')

max_score = 0
for i in range(trees.shape[1] - 2):
    for j in range(trees.shape[0] - 2):
        x, y = i + 1, j + 1
        height = trees[y, x]
        scores = [0, 0, 0, 0]  # U L R D
        for x_left in range(x - 1, -1, -1):
            if trees[y, x_left] >= height:
                scores[1] += 1
                break
            else:
                scores[1] += 1
        for x_right in range(x + 1, trees.shape[1]):
            if trees[y, x_right] >= height:
                scores[2] += 1
                break
            else:
                scores[2] += 1
        for y_up in range(y - 1, -1, -1):
            if trees[y_up, x] >= height:
                scores[0] += 1
                break
            else:
                scores[0] += 1
        for y_down in range(y + 1, trees.shape[0]):
            if trees[y_down, x] >= height:
                scores[3] += 1
                break
            else:
                scores[3] += 1
        total_score = np.prod(scores)
        # print(f'Score at x = {x}, y = {y} = {total_score} --> {scores}')
        max_score = max(max_score, total_score)
print(f'The answer to part 2 = {max_score}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
