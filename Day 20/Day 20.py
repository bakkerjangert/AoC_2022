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


def increase_marker(string):
    if string[-1] != 'z':
        string = string[:-1] + chr(ord(string[-1]) + 1)
    elif string[-2] != 'z':
        string = string[0] + chr(ord(string[1]) + 1) + 'a'
    else:
        string = chr(ord(string[0]) + 1) + 'aa'
    return string

data = list()
marker = 'aaa'

for number in lines:
    data.append(marker + number)
    marker = increase_marker(marker)
data_order = data.copy()

for number in data_order:
    current_index = data.index(number)
    goal_index = current_index + int(number[3:])
    if goal_index >= len(data):
        goal_index = goal_index % len(data) + 1
    if goal_index < -len(data):
        goal_index = -(-goal_index % len(data)) - 1
    if goal_index != 0:
        data.insert(goal_index, data.pop(current_index))
    else:
        data.append(data.pop(current_index))
    # for n in data:
    #     print(n[3:], end=', ')
    # print('')

mixed_data = deque()
index_0 = None
for i, number in enumerate(data):
    mixed_data.append(int(number[3:]))
    if mixed_data[-1] == 0:
        index_0 = i
mixed_data.rotate(-1 * index_0)

n1 = mixed_data[1000 % len(mixed_data)]
n2 = mixed_data[2000 % len(mixed_data)]
n3 = mixed_data[3000 % len(mixed_data)]

print(f'{n1} + {n2} + {n3} = {n1 + n2 + n3}')

# Part 2
factor = 811_589_153
# factor = 1
rounds = 10
# rounds = 1
data = deque()
data_order = dict()
marker = 'aaa'
zero = None

for number in lines:
    n1 = int(number)
    n2 = int(number) * factor
    f = int(number) * factor
    if n1 == 0:
        zero = marker + str(n2)
    data.append(marker + str(n2))
    data_order[marker + str(n2)] = f
    marker = increase_marker(marker)

# for n2 in data:
#     print(n2[3:], end=', ')
# print('')

for _ in range(rounds):
    for number in sorted(data_order.keys()):
        n = int(number[3:])
        current_index = data.index(number)
        val = data[current_index]
        data.remove(val)
        data.rotate(-n)
        data.insert(current_index, val)
    for n2 in data:
        print(n2, end=', ')
    print('')

index_0 = data.index(zero)
data.rotate(-1 * index_0)

for n2 in data:
    print(data_order[n2], end=', ')
print('')

val_n1 = data[1000 % len(data)]
val_n2 = data[2000 % len(data)]
val_n3 = data[3000 % len(data)]

n1 = data_order[val_n1]
n2 = data_order[val_n2]
n3 = data_order[val_n3]
print(f'{n1} + {n2} + {n3} = {n1 + n2 + n3}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')