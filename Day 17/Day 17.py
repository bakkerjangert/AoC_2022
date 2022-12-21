import time
import numpy as np
from copy import deepcopy
from collections import deque
# Advent of Code 2022 - Day 15 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()

def print_status(grid):
    print(f'\nCurrent state')
    for line in grid[:]:
        print(' ' * 2 + ''.join(line))


def check_repeat(grid):
    # print_status(grid)
    if grid.shape[0] % 2 == 1:
        return False
    top = grid[: grid.shape[0] // 2]
    bottom = grid[grid.shape[0] // 2:]
    if np.array_equal(top, bottom):
        print('\nNext block')
        for i in range(top.shape[0]):
            print(''.join(top[i]) + '  @  ' + ''.join(bottom[i]))
        return True
    return False


block_1 = [[0, 3], [0, 4], [0, 5], [0, 6]]
block_2 = [[0, 4], [1, 3], [1, 4], [1, 5], [2, 4]]
block_3 = [[0, 5], [1, 5], [2, 5], [2, 4], [2, 3]]
block_4 = [[0, 3], [1, 3], [2, 3], [3, 3]]
block_5 = [[0, 3], [0, 4], [1, 3], [1, 4]]

blocks = (block_1, block_2, block_3, block_4, block_5)
jets = deque(lines[0])

jet_key = {'<': -1, '>': 1}

grid = np.zeros((4, 9), dtype=str)
grid[:] = '.'
grid[:, 0], grid[:, -1] = chr(9474), chr(9474)
grid[-1] = chr(9472)
grid[-1, 0], grid[-1, -1] = chr(9532), chr(9532)

row = np.zeros((1, 9), dtype=str)
row[:], row[0, 0], row[0, -1] = '.', chr(9474), chr(9474)

block_number = 0
goal_pt1 = 2022
goal = 1000000000000
initial_blocks = 100  # before starting to search for repeating pattern
block_data = dict()
skip_lines = 200
checker, stage = None, 0
pt1_found, pt2_found = False, False
start_block, end_block = None, None

while block_number < goal + 1:
    if pt1_found and pt2_found:
        break
    for block in blocks:
        if pt1_found and pt2_found:
            break
        block_number += 1
        # print(f'block number = {block_number}')
        block = deepcopy(block)
        while '#' not in grid[0]:
            if chr(9472) in grid[0]:
                break
            grid = np.delete(grid, (0), axis=0)
        # Check if part 1 is found
        if block_number == goal_pt1 + 1:
            print(f'Answer part 1 = {grid.shape[0] - 1}')
            pt1_found = True
        if block_number % 1000 == 0 and stage == 0:
            line_1 = grid[skip_lines - 1]
            for i in range(grid.shape[0] - skip_lines):
                line_2 = grid[skip_lines + i]
                if np.array_equal(line_1, line_2):
                    if skip_lines + 2 * i < grid.shape[0]:
                        sub_grid = grid[skip_lines - 1: skip_lines + 2 * i + 1]
                        check = check_repeat(sub_grid)
                        if check and sub_grid.shape[0] > 6:
                            print(f'Duplicate found')
                            checker = sub_grid[:sub_grid.shape[0] // 2]
                            stage += 1
                            print(f'Block = {block_number}')
                            break
        if stage == 2 and not pt2_found:
            delta_block += 1
            if grid.shape[0] - heigth <= checker.shape[0]:
                block_data[delta_block] = grid.shape[0] - heigth
                print(f'{delta_block} --> {block_data[delta_block]}')
            else:
                end_block = block_number - 1
                new_goal = goal - end_block
                print(new_goal)
                cycles =  new_goal // max(block_data.keys())
                rest_blocks = new_goal % max(block_data.keys())
                total_rows = (grid.shape[0] - 1) + cycles * checker.shape[0] + block_data[rest_blocks]
                print(f'The answer to part 2 = {total_rows}')
                pt2_found = True
        if stage == 1:
            if np.array_equal(grid[20:checker.shape[0]], checker[20:]):
                print('HERE!!!')
                start_block = block_number
                delta_block = 0
                heigth = grid.shape[0]
                print(f'start block = {start_block}')
                stage += 1
        for r in range(3 + block[-1][0] + 1):
            grid = np.r_[row,  grid]
        # # Show Next Block
        # sub_grid = grid.copy()
        # for cell in block:
        #     sub_grid[cell[0], cell[1]] = '@'
        # print_status(sub_grid)
        falling = True
        while falling:
            # Jet push
            push = jet_key[jets[0]]
            jets.rotate(-1)
            shift = True
            for cell in block:
                if grid[cell[0], cell[1] + push] != '.':
                    shift = False
                    break
            if shift:
                for cell in block:
                    cell[1] += push
            # fall
            for cell in block:
                if grid[cell[0] + 1, cell[1]] != '.':
                    falling = False
                    for pos in block:
                        grid[pos[0], pos[1]] = '#'
                    break
            if falling:
                for cell in block:
                    cell[0] += 1


# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
