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

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
