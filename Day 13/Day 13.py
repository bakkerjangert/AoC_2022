import time
import math
import sys
import ast

# Advent of Code 2022 - Day 10 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()

def check_list(left, right):
    # print(f'Compare {left} - {right}')
    found = False
    while True:
        # print(f'left = {left}, right = {right}')
        if len(left) == 0 and len(right) > 0:
            # print(f'Ánswer += {index}')
            correct_order[0] = True
            answer[0] += index
            return True
        elif len(left) > 0 and len(right) == 0:
            return True
        elif len(left) == 0 and len(right) == 0:
            return False
        else:
            new_left, new_right = left.pop(0), right.pop(0)
            # print(new_left, new_right)
            if type(new_left) != type(new_right):
                if type(new_left) == type(0):
                    new_left = [new_left]
                else:
                    new_right = [new_right]
            if type(new_left) == type([]):
                found = check_list(new_left, new_right)
            else:
                found = check_int(new_left, new_right)
        if found:
            return True

def check_int(left, right):
    # print(f'Compare {left} - {right}')
    if left < right:
        # print(f'Ánswer += {index}')
        correct_order[0] = True
        answer[0] += index
        return True
    elif left > right:
        return True
    else:
        return False

correct_order = [False]
answer = [0]
for i in range(len(lines) // 3 + 1):
    index = i + 1
    # print(f'Checking pair {index}')
    left = ast.literal_eval(lines[i * 3])
    right = ast.literal_eval(lines[i * 3 + 1])
    check_list(left, right)

print(f'The answer to part 1 = {answer[0]}')

orders = dict()
divider_1 = '[[2]]'
divider_2 = '[[6]]'

for x in (divider_1, divider_2):
    lines.append(x)

for line_1 in lines:
    if line_1 == '':
        continue
    left = ast.literal_eval(line_1)
    for line_2 in lines:
        if line_2 == '' or line_1 == line_2:
            continue
        correct_order[0] = False
        left = ast.literal_eval(line_1)
        right = ast.literal_eval(line_2)
        check_list(left, right)
        if correct_order[0]:
            if line_1 not in orders.keys():
                orders[line_1] = [line_2]
            else:
                orders[line_1].append(line_2)
new_order = []
for line in lines:
    if line == '':
        continue
    if line not in orders.keys():
        # print(f'Last line = {line}')
        new_order.append(line)

while len(orders) != 0:
    target = new_order[0]
    # if line not in orders.keys():
    #     break
    for key in list(orders.keys()):
        if target in orders[key]:
            for line in new_order[1:]:
                if line in orders[key]:
                    orders[key].remove(line)
            if len(orders[key]) == 1:
                if orders[key][0] == target:
                    new_order.insert(0, key)
                    del orders[key]

# for line in new_order:
#     print(line)

print(f'Tha answer to part 2 = {(new_order.index(divider_1) + 1) * (new_order.index(divider_2) + 1)}')

# print(orders)
# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
