import time
import numpy as np
# Advent of Code 2022 - Day 15 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
y = 2_000_000
xy_max = 4_000_000
# file = 'test.txt'
# y = 10
# xy_max = 20

with open(file) as f:
    lines = f.read().splitlines()

beacons_y = set()
covered_y = set()

for l in lines:
    sx, sy = int(l.split('x=')[1].split(',')[0]), int(l.split('y=')[1].split(':')[0])
    bx, by = int(l.split('x=')[2].split(',')[0]), int(l.split('y=')[2])
    manhattan = abs(sx - bx) + abs(sy - by)
    if by == y:
        beacons_y.add(bx)
    if sy - manhattan <= y <= sy + manhattan:
        width = 1 + 2 * (manhattan - abs(sy - y))
        x = sx - width // 2
        for dx in range(width):
            covered_y.add(x)
            x += 1
print(f'The answer to part 1 = {len(covered_y) - len(beacons_y)}')


def check_linked_ranges(ranges):
    # print(f'Old ranges = {ranges}')
    if len(ranges) <= 1:
        return ranges
    finished = False
    while not finished:
        finished = True
        for i in range(len(ranges) - 1):
            if ranges[i][1] + 1 == ranges[i + 1][0]:
                r1, r2 = ranges[i][0], ranges[i + 1][1]
                ranges = ranges[:i] + [[r1, r2]] + ranges[i + 2:]
                finished = False
                break
    # print(f'New ranges = {ranges}')
    return ranges


def update_ranges(new_range, old_ranges):
    if len(old_ranges) == 0:
        return [new_range]
    elif len(old_ranges) == 1:
        r = old_ranges[0]
        if r[0] <= new_range[0] <= r[1] or r[0] <= new_range[1] <= r[1]:
            new_ranges = [[min(r[0], new_range[0]), max(r[1], new_range[1])]]
        elif new_range[0] < r[0]:
            new_ranges = [new_range, r]
        else:
            new_ranges = [r, new_range]
        return new_ranges
    elif new_range[1] < old_ranges[0][0]:
        return [new_range] + old_ranges
    elif old_ranges[-1][1] < new_range[0]:
        return old_ranges + [new_range]
    inside_start, inside_end = None, None
    between_start, between_end = None, None
    xs, xe = new_range[0], new_range[1]
    # Hack to prevent corner case
    if xs < old_ranges[0][0]:
        old_ranges[0][0] = xs
    if old_ranges[-1][1] < xe:
        old_ranges[-1][1] = xe
    # End Hack
    for i, cur_range in enumerate(old_ranges):
        if cur_range[0] <= xs <= cur_range[1]:
            inside_start = i
        if cur_range[0] <= xe <= cur_range[1]:
            inside_end = i
        if i != len(old_ranges) - 1:
            if cur_range[1] < xs < old_ranges[i + 1][0]:
                between_start = i
            if cur_range[1] < xe < old_ranges[i + 1][0]:
                between_end = i
    if (inside_start, inside_end, between_start, between_end).count(None) != 2:
        print('Warning --> Not two None values found')
    left_side = old_ranges[:inside_start] if between_start is None else old_ranges[:between_start + 1]
    right_side = old_ranges[inside_end + 1:] if between_end is None else old_ranges[between_end + 1:]
    mid_0 = xs if between_start is not None else old_ranges[inside_start][0]
    mid_1 = xe if between_end is not None else old_ranges[inside_end][1]
    return left_side + [[mid_0, mid_1]] + right_side


ranges = dict()
for i in range(0, xy_max + 1):
    ranges[i] = []

print('Generated dict')
for i, l in enumerate(lines):
    print(f'processing line {i + 1} of {len(lines)}')
    sx, sy = int(l.split('x=')[1].split(',')[0]), int(l.split('y=')[1].split(':')[0])
    bx, by = int(l.split('x=')[2].split(',')[0]), int(l.split('y=')[2])
    manhattan = abs(sx - bx) + abs(sy - by)
    min_y, max_y = sy - manhattan, sy + manhattan
    sub_range = [sx, sx]
    for cur_y in range(min_y, max_y + 1):
        # print(cur_y, sub_range)
        if 0 <= cur_y <= xy_max:
            limited_sub_range = [max(0, sub_range[0]), min(sub_range[1], xy_max)]
            ranges[cur_y] = update_ranges(limited_sub_range, ranges[cur_y])
            ranges[cur_y] = check_linked_ranges(ranges[cur_y])
        if cur_y < sy:
            sub_range[0] -= 1
            sub_range[1] += 1
        else:
            sub_range[0] += 1
            sub_range[1] -= 1

goal_x, goal_y = None, None
for key in ranges.keys():
    if ranges[key][0] != [0, xy_max]:
        if len(ranges[key]) > 1:
            goal_x = ranges[key][0][1] + 1
        elif ranges[key][0][1] != 0:
            goal_x = 0
        else:
            goal_x = xy_max
        goal_y = key
print(goal_x, goal_y)
print(f'The answer to part 2 = {4000000 * goal_x + goal_y}')

# for key in ranges.keys():
#     print(key, ranges[key])

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
