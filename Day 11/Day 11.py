import time
import math
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


class Monkey:
    def __init__(self, monkey, items, operator_val, operator, test_val, monkey_if_true, monkey_if_false):
        self.monkey = monkey
        self.items = items
        self.operator_val = operator_val
        self.operator = operator
        self.test_val = test_val
        self.monkey_if_false = monkey_if_false
        self.monkey_if_true = monkey_if_true
        self.inspections = 0
        self.divider = 3
        self.counter = 0

    def play(self):
        for i in range(len(self.items)):
            self.inspections += 1
            item = self.items.pop(0)
            if self.operator == '+':
                item = item + self.operator_val if self.operator_val != 'old' else item + item
            elif self.operator == '*':
                item = item * self.operator_val if self.operator_val != 'old' else item * item
            if self.divider == 3:
                item = item // self.divider
            else:
                item = item % self.divider
            if item % self.test_val == 0:
                monkeys[self.monkey_if_true].items.append(item)
            else:
                monkeys[self.monkey_if_false].items.append(item)

monkeys = dict()
for i, monkey in enumerate(range(len(lines) // 7 + 1)):
    items = list(map(int, lines[i * 7 + 1].split(': ')[-1].split(', ')))
    try:
        operator_val = int(lines[i * 7 + 2].split(' ')[-1])
    except ValueError:
        operator_val = lines[i * 7 + 2].split(' ')[-1]
    operator = lines[i * 7 + 2].split(' ')[-2]
    test_val = int(lines[i * 7 + 3].split(' ')[-1])
    monkey_if_true = int(lines[i * 7 + 4].split(' ')[-1])
    monkey_if_false = int(lines[i * 7 + 5].split(' ')[-1])
    monkeys[i] = Monkey(i, items, operator_val, operator, test_val, monkey_if_true, monkey_if_false)


for round in range(20):
    for monkey in range(len(monkeys)):
        monkeys[monkey].play()

inspection_values = []
for monkey in range(len(monkeys)):
    inspection_values.append(monkeys[monkey].inspections)
inspection_values.sort(reverse=True)
print(f'The answer to part 1 = {inspection_values[0] * inspection_values[1]}')

# Part 2
monkeys = dict()
dividers = []

for i, monkey in enumerate(range(len(lines) // 7 + 1)):
    items = list(map(int, lines[i * 7 + 1].split(': ')[-1].split(', ')))
    try:
        operator_val = int(lines[i * 7 + 2].split(' ')[-1])
    except ValueError:
        operator_val = lines[i * 7 + 2].split(' ')[-1]
    operator = lines[i * 7 + 2].split(' ')[-2]
    test_val = int(lines[i * 7 + 3].split(' ')[-1])
    monkey_if_true = int(lines[i * 7 + 4].split(' ')[-1])
    monkey_if_false = int(lines[i * 7 + 5].split(' ')[-1])
    monkeys[i] = Monkey(i, items, operator_val, operator, test_val, monkey_if_true, monkey_if_false)
    dividers.append(monkeys[i].test_val)

lcm = math.lcm(*dividers)
print(lcm, type(lcm))

for monkey in range(len(monkeys)):
    monkeys[monkey].divider = lcm

for round in range(10_000):
    for monkey in range(len(monkeys)):
        monkeys[monkey].play()
        # print(f'Monkey {monkey} has {monkeys[monkey].inspections} inspections at round {round + 1}')
    if (round + 1) % 1000 == 0 or round in (0, 19):
        print(f'Round {round + 1}')
        for monkey in range(len(monkeys)):
            print(f'Monkey {monkey} inspected {monkeys[monkey].inspections}')

inspection_values = []
for monkey in range(len(monkeys)):
    inspection_values.append(monkeys[monkey].inspections)
inspection_values.sort(reverse=True)
print(f'The answer to part 2 = {inspection_values[0] * inspection_values[1]}')

# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
