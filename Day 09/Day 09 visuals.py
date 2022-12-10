import time
import numpy as np


# Advent of Code 2022 - Day 09 part 1 & 2
# https://adventofcode.com/2022/day/9

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file) as f:
    lines = f.read().splitlines()

x_bound, y_bound = [0, 0], [0, 0]
x, y = 0, 0

for line in lines:
    delta = int(line.split()[-1])
    if line[0] == 'U':
        y -= delta
        y_bound[0] = min(y_bound[0], y)
    if line[0] == 'D':
        y += delta
        y_bound[1] = max(y_bound[1], y)
    if line[0] == 'L':
        x -= delta
        x_bound[0] = min(x_bound[0], x)
    if line[0] == 'R':
        x += delta
        x_bound[1] = max(x_bound[1], x)

size_x = x_bound[1] - x_bound[0] + 1
size_y = y_bound[1] - y_bound[0] + 1
start = (x_bound[0], -y_bound[0])

board = np.zeros((size_y, size_x), dtype=str)
board[:] = '.'

tail_trail = np.copy(board)
tail_trail[start[1], start[0]] = '#'


def move_tail():
    for x in (pos_head[0] - 1, pos_head[0], pos_head[0] + 1):
        for y in (pos_head[1] - 1, pos_head[1], pos_head[1] + 1):
            if pos_tail[0] == x and pos_tail[1] == y:
                return None
    pos_tail[0] = prev_pos_head[0]
    pos_tail[1] = prev_pos_head[1]
    tail_trail[pos_tail[1], pos_tail[0]] = '#'


def move_tail_pt2(a, b, tail):
    # Pass if in range
    for x in (a[0] - 1, a[0], a[0] + 1):
        for y in (a[1] - 1, a[1], a[1] + 1):
            if b[0] == x and b[1] == y:
                return b
    goals_direct = ((a[0] - 1, a[1]), (a[0] + 1, a[1]), (a[0], a[1] - 1), (a[0], a[1] + 1))
    goals_diagonal = ((a[0] - 1, a[1] - 1), (a[0] + 1, a[1] + 1), (a[0] + 1, a[1] - 1), (a[0] - 1, a[1] + 1))
    # Direct goals
    for x in (b[0] - 1, b[0], b[0] + 1):
        for y in (b[1] - 1, b[1], b[1] + 1):
            if (x, y) in goals_direct:
                b[0] = x
                b[1] = y
                if tail:
                    tail_trail[b[1], b[0]] = '#'
                return b
    # diagonal goals
    for x in (b[0] - 1, b[0], b[0] + 1):
        for y in (b[1] - 1, b[1], b[1] + 1):
            if (x, y) in goals_diagonal:
                b[0] = x
                b[1] = y
                if tail:
                    tail_trail[b[1], b[0]] = '#'
                return b

def print_pos():
    print(f'\nCurrent board layout\n')
    positions = board.copy()
    positions[start[1], start[0]] = 's'
    positions[pos_head[1], pos_head[0]] = 'H'
    positions[pos_tail[1], pos_tail[0]] = 'T'
    print(positions)


def print_pos_pt2():
    print(f'\nCurrent board layout\n')
    positions = board.copy()
    positions[start[1], start[0]] = 's'
    for part in list('H123456789'):
        positions[parts[part][1][1], parts[part][1][0]] = part
    print(positions)

pos_head, pos_tail = list(start), list(start)

for line in lines:
    for step in range(int(line.split()[-1])):
        prev_pos_head = pos_head.copy()
        if line[0] == 'U':
            pos_head[1] -= 1
        if line[0] == 'D':
            pos_head[1] += 1
        if line[0] == 'L':
            pos_head[0] -= 1
        if line[0] == 'R':
            pos_head[0] += 1
        move_tail()
        # print_pos()

# for i in range(tail_trail.shape[0]):
#     line = tail_trail[i]
#     print(''.join(line))

print(f'The answer to part 1 = {np.count_nonzero(tail_trail == "#")}')

# PART 2
parts = dict()
directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
for part in list('H123456789'):
    parts[part] = [list(start), list(start)]

tail_trail = np.copy(board)
tail_trail[start[1], start[0]] = '#'

for line in lines:
    for step in range(int(line.split()[-1])):
        parts['H'][0] = parts['H'][1].copy()
        if line[0] == 'U':
            parts['H'][1][1] -= 1
        if line[0] == 'D':
            parts['H'][1][1] += 1
        if line[0] == 'L':
            parts['H'][1][0] -= 1
        if line[0] == 'R':
            parts['H'][1][0] += 1
        _ = 'H12345678'
        for i, part in enumerate(list('123456789')):
            parts[part][0] = parts[part][1].copy()
            tail = True if part == '9' else False
            next_pos = move_tail_pt2(parts[_[i]][1], parts[part][1], tail)
            parts[part][1] = next_pos
        # print_pos_pt2()

# for i in range(tail_trail.shape[0]):
#     line = tail_trail[i]
#     print(''.join(line))

print(f'The answer to part 2 = {np.count_nonzero(tail_trail == "#")}')
# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')