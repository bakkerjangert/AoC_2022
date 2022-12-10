import time
import numpy as np
import sys

# Advent of Code 2022 - Day 09 part 1 & 2
# https://adventofcode.com/2022/day/9

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file) as f:
    lines = f.read().splitlines()

directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def solve(sequence):
    def move_var1(a, b):
        # Pass if in range
        for x in (a[0] - 1, a[0], a[0] + 1):
            for y in (a[1] - 1, a[1], a[1] + 1):
                if b[0] == x and b[1] == y:
                    return b
        goals_cross = ((a[0] - 1, a[1]), (a[0] + 1, a[1]), (a[0], a[1] - 1), (a[0], a[1] + 1))
        goals_diagonal = ((a[0] - 1, a[1] - 1), (a[0] + 1, a[1] + 1), (a[0] + 1, a[1] - 1), (a[0] - 1, a[1] + 1))
        # Try to reach adjacent goals
        for x in (b[0] - 1, b[0], b[0] + 1):
            for y in (b[1] - 1, b[1], b[1] + 1):
                if (x, y) in goals_cross:
                    b[0], b[1] = x, y
                    return b
        # Try to reach diagonal goals
        for x in (b[0] - 1, b[0], b[0] + 1):
            for y in (b[1] - 1, b[1], b[1] + 1):
                if (x, y) in goals_diagonal:
                    b[0], b[1] = x, y
                    return b
    def move_var2(a, b):
        # Pass if in range
        range_a, range_b = list(), list()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                range_a.append((a[0] + dx, a[1] + dy))
                range_b.append((b[0] + dx, b[1] + dy))
        collides = set(range_a) & set(range_b)
        if tuple(b) in range_a:
            return b
        for coord in collides:
            if coord[0] == a[0] or coord[1] == a[1]:
                b[0], b[1] = coord[0], coord[1]
                return b
        # Try to reach diagonal goals
        for coord in collides:
            b[0], b[1] = coord[0], coord[1]
            return b
    tail_trail = set()
    parts = dict()
    head, tail = sequence[0], sequence[-1]
    for part in sequence:
        parts[part] = [0, 0]
    for line in lines:
        for step in range(int(line.split()[-1])):
            for i in range(2):
                parts[head][i] += directions[line[0]][i]
            for i, part in enumerate(sequence[1:]):
                parts[part] = move_var2(parts[sequence[i]], parts[part])
            tail_trail.add(tuple(parts[tail]))
    print(f'The answer is {len(tail_trail)}')

solve('HT')
solve('H123456789')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
