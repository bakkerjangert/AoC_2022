import time
import numpy as np
# Advent of Code 2022 - Day 14 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()

def print_grid():
    print(f'\nCurrent state:')
    for line in grid[:]:
        print(''.join(line))

def print_grid_2():
    print(f'\nCurrent state:')
    for line in grid_pt2[:]:
        print(''.join(line))

x_min, x_max, y_min, y_max = 999999, -100, 999999, -100

rock_parts = set()
for line in lines:
    parts = line.split(' -> ')[:]
    for i, part in enumerate(parts):
        if i == len(parts) - 1:
            break
        x1, y1 = int(parts[i].split(',')[0]), int(parts[i].split(',')[1])
        x2, y2 = int(parts[i + 1].split(',')[0]), int(parts[i + 1].split(',')[1])
        rock_parts.add((x1, y1))
        x_min, x_max = min(x1, x_min), max(x1, x_max)
        y_min, y_max = min(y1, y_min), max(y1, y_max)
        dx, dy = x2 - x1, y2 - y1
        if dx != 0:
            factor = 1 if dx > 0 else -1
            for _ in range(abs(dx)):
                x1 += 1 * factor
                rock_parts.add((x1, y1))
            x_min, x_max = min(x1, x_min), max(x1, x_max)
        if dy != 0:
            factor = 1 if dy > 0 else -1
            for _ in range(abs(dy)):
                y1 += 1 * factor
                rock_parts.add((x1, y1))
            y_min, y_max = min(y1, y_min), max(y1, y_max)

grid = np.zeros((y_max + 1, x_max - x_min + 1), dtype=str)
grid[:] = '.'
grid[0, 500 - x_min] = '+'

for rock in rock_parts:
    grid[rock[1], rock[0] - x_min] = '#'
grid_pt2 = np.copy(grid)

bottom_found = False
sand_grains = 0

while True:
    drop = [500 - x_min, 0]
    while True:
        if drop[1] == len(grid[:]) - 1:
            bottom_found = True
            break
        if grid[drop[1] + 1, drop[0]] == '.':
            drop[1] += 1
        elif grid[drop[1] + 1, drop[0] - 1] == '.':
            drop[1] += 1
            drop[0] -= 1
        elif grid[drop[1] + 1, drop[0] + 1] == '.':
            drop[1] += 1
            drop[0] += 1
        else:
            grid[drop[1], drop[0]] = 'o'
            sand_grains += 1
            # print_grid()
            break
    if bottom_found:
        break

print(f'The answer to part 1 = {sand_grains}')

# Part 2
sand_grains = 0

new_row = np.zeros(len(grid_pt2[0]), dtype='str')
new_row[:] = '.'

for i in range(2):
    grid_pt2 = np.vstack([grid_pt2, new_row])

new_col = np.zeros(len(grid_pt2[:]), dtype='str')
new_col[:] = '.'

grid_pt2 = np.c_[new_col, new_col, grid_pt2, new_col, new_col]
x_min -= 2

grid_pt2[-1] = '#'
grid_pt2[:, [0, -1]] = '#'

# print_grid_2()
total_fill = False
while True:
    drop = [500 - x_min, 0]
    while True:
        if grid_pt2[drop[1] + 1, drop[0]] == '.':
            drop[1] += 1
        elif grid_pt2[drop[1] + 1, drop[0] - 1] == '.':
            drop[1] += 1
            drop[0] -= 1
        elif grid_pt2[drop[1] + 1, drop[0] + 1] == '.':
            drop[1] += 1
            drop[0] += 1
        else:
            grid_pt2[drop[1], drop[0]] = 'o'
            sand_grains += 1
            if drop[1] == 0:
                total_fill = True
            break
    if total_fill:
        break
print_grid_2()

n1, n2 = ''.join(grid_pt2[:, 1]).count('o') - 1, ''.join(grid_pt2[:, -2]).count('o') - 1
sand_grains += n1 * (n1 + 1) // 2 + n2 * (n2 + 1) // 2

print(f'The answer to part 2 = {sand_grains}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
