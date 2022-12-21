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


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def equal(a, b):
    return (True, a, b) if int(a) == int(b) else (False, a, b)


keys = {'+': add, '-': subtract, '*': multiply, '/': divide, '=': equal}

waiting_monkeys = dict()
finished_monkeys = dict()

for line in lines:
    monkey = line.split(':')[0]
    if line[6] in 'abcdefghijklmnopqrstuvwxyz':
        waiting_monkeys[monkey] = line.split(' ')[1:]
    elif line[6] in '0123456789':
        finished_monkeys[monkey] = int(line.split(' ')[1])


def run(waiting_monkeys, finished_monkeys, pt_1=False, pt_2=False):
    while len(waiting_monkeys) > 0:
        for monkey in list(waiting_monkeys.keys()).copy():
            data = waiting_monkeys[monkey]
            monkey_a, monkey_b = data[0], data[2]
            # print(monkey_a, monkey_b)
            if monkey_a in finished_monkeys.keys() and monkey_b in finished_monkeys.keys():
                val = keys[data[1]](finished_monkeys[monkey_a], finished_monkeys[monkey_b])
                finished_monkeys[monkey] = val
                del waiting_monkeys[monkey]
    if pt_1:
        print(f'The answer to part 1 = {int(finished_monkeys["root"])}')
    if pt_2:
        return finished_monkeys['root']


run(deepcopy(waiting_monkeys), deepcopy(finished_monkeys), pt_1=True)

finished_monkeys['humn'] = 0
waiting_monkeys['root'][1] = '='
finished = False

v0 = run(deepcopy(waiting_monkeys), deepcopy(finished_monkeys), pt_2=True)
finished_monkeys['humn'] = 1
v1 = run(deepcopy(waiting_monkeys), deepcopy(finished_monkeys), pt_2=True)
while not finished:
    d0 = v0[1] - v0[2]
    d1 = v1[1] - v1[2]
    finished_monkeys['humn'] += d0 // (d0 - d1)
    v0 = run(deepcopy(waiting_monkeys), deepcopy(finished_monkeys), pt_2=True)
    if v0[0]:
        finished = True
        break
    finished_monkeys['humn'] += 1
    v1 = run(deepcopy(waiting_monkeys), deepcopy(finished_monkeys), pt_2=True)
    if v1[0]:
        finished = True
        break
    print(v0, v1)
print(f'The answer to part 2 = {int(finished_monkeys["humn"])}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')