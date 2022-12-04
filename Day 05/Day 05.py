import time
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1

# Part 2


toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
