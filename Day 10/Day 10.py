import time
import numpy as np
import sys

# Advent of Code 2022 - Day 10 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file) as f:
    lines = f.read().splitlines()

x, cycle = 1, 1
read_cycle = 20
delta_cycle = 40
answer = 0

def draw():
    if string_index in sprite:
        return '#'
    else:
        return ' '

sprite = [0, 1, 2]
string = ''
strings = []
string_index = 0

for line in lines:
    i = 1 if line == 'noop' else 2
    for step in range(i):
        string += draw()
        string_index += 1
        if string_index == 40:
            strings.append(string)
            string = ''
            string_index = 0
        # print(cycle, x)
        cycle += 1
        if step == 1:
            x += int(line.split()[-1])
            for _, delta in enumerate((-1, 0 ,1)):
                sprite[_] = x + delta
        if cycle == read_cycle or (cycle - read_cycle) % delta_cycle == 0:
            answer += x * cycle
print(f'The answer to part 1 = {answer}')
print(f'The answer to part 2:')
for line in strings:
    print(line)


# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
