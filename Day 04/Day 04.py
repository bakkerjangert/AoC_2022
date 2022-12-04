import time
# Advent of Code 2022 - Day 04 part 1 & 2
# https://adventofcode.com/2022/day/4
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()

data = []

for line in lines:
    line = line.replace(',', '-')
    data.append(list(map(int, line.split('-'))))

# Part 1
answer = 0
for row in data:
    if (row[0] <= row[2] and row[1] >= row[3]) or (row[0] >= row[2] and row[1] <= row[3]):
        answer += 1
print(f'Part 1:\nThe answer is = {answer}')

# Part 2
answer = 0
for row in data:
    if row[2] <= row[0] <= row[3] or row[2] <= row[1] <= row[3] or row[0] <= row[2] <= row[1] or row[0] <= row[3] <= row[1]:
        answer += 1
print(f'\nPart 2:\nThe answer is = {answer}')
toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
