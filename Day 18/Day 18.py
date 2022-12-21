import time
import numpy as np
from copy import deepcopy
from collections import deque
# Advent of Code 2022 - Day 15 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()

def get_suspects(p1):
    next_points = set()
    # direct
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                p2 = (p1[0] + dx, p1[1] + dy, p1[2] + dz)
                if p1 == p2 or p2 in points or p2 in total_lining:
                    continue
                for dp in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
                    p3 = (p2[0] + dp[0], p2[1] + dp[1], p2[2] + dp[2])
                    if p3 in points:
                        next_points.add(p2)
                        break
    return next_points

open_sides = 0
points = set()

for line in lines:
    points.add(tuple(map(int, line.split(','))))

for p1 in points:
    sides = 6
    for dp in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
        p2 = (p1[0] + dp[0], p1[1] + dp[1], p1[2] + dp[2])
        if p2 in points:
            sides -= 1
    open_sides += sides
print(f'The answer to part 1 = {open_sides}')

outerpoint = sorted(points)[0]
linging_point = (outerpoint[0] - 1, outerpoint[1], outerpoint[2])

unchecked_lining = {linging_point}
total_lining = set()

while len(unchecked_lining) > 0:
    p = unchecked_lining.pop()
    total_lining.add(p)
    next_linings = get_suspects(p)
    unchecked_lining = unchecked_lining | next_linings
    print(len(unchecked_lining))

sides_pt2 = 0
for p1 in total_lining:
    for dp in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
        p2 = (p1[0] + dp[0], p1[1] + dp[1], p1[2] + dp[2])
        if p2 in points:
            sides_pt2 += 1

print(f'The answer to part 2 = {sides_pt2}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
