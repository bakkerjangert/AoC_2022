import time
# Advent of Code 2022 - Day 02 part 1 & 2
# https://adventofcode.com/2022/day/2
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()

# Elf --> A = Rock, B = Paper, C = Scissors

# Part 1
# You --> X = Rock, Y = Paper, Z = Scissors
personal_score = {'X': 1, 'Y': 2, 'Z': 3}  # to optimize add personal and round score in one dict
round_score = {'A X': 3, 'A Y': 6, 'A Z': 0,
               'B X': 0, 'B Y': 3, 'B Z': 6,
               'C X': 6, 'C Y': 0, 'C Z': 3}
score = 0
for line in lines:
    score += personal_score[line[-1]] + round_score[line]

print(f'Part 1:\nYour total score = {score}')

# Part 2
# You --> X = Lose, Y = Draw, Z = Win
round_score = {'X': 0, 'Y': 3, 'Z': 6}  # to optimize add personal and round score in one dict
personal_score = {'A X': 3, 'A Y': 1, 'A Z': 2,
                  'B X': 1, 'B Y': 2, 'B Z': 3,
                  'C X': 2, 'C Y': 3, 'C Z': 1}
score = 0
for line in lines:
    score += personal_score[line] + round_score[line[-1]]

print(f'\nPart 2:\nYour total score = {score}')

toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')