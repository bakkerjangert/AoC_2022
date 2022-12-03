import time
# Advent of Code 2022 - Day 03 part 1 & 2
# https://adventofcode.com/2022/day/3
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()

priorities = dict()
lower_string = 'abcdefghijklmnopqrstuvwxyz'
upper_string = lower_string.upper()
total_string = lower_string + upper_string

for i, score in enumerate(range(1, 53)):
    priorities[total_string[i]] = score

# Part 1
answer_part1 = 0
for line in lines:
    left_part = line[0: len(line) // 2]
    right_part = line[len(line) // 2:]
    for letter in left_part:
        if letter in right_part:
            answer_part1 += priorities[letter]
            break
print(f'Part 1:\nThe sum of priorities = {answer_part1}')

# Part 2
answer_part2 = 0
for i in range(len(lines) // 3):
    for letter in lines[i * 3]:
        if letter in lines[i * 3 + 1] and letter in lines[i * 3 + 2]:
            answer_part2 += priorities[letter]
            break
print(f'\nPart 2:\nThe sum of priorities = {answer_part2}')
toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
