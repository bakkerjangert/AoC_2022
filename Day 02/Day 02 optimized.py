import time
from collections import Counter
# Advent of Code 2022 - Day 02 part 1 & 2
# https://adventofcode.com/2022/day/2
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()
data = Counter(lines)  # Generates dict with unique entries with the times they appear

# Elf --> A = Rock, B = Paper, C = Scissors
# Score --> Rock = 1, Paper = 2, Scissors = 3
# Score --> Lose = 0, Draw = 3, Win = 6
# For total score just add both score lines together

# Part 1
# You --> X = Rock, Y = Paper, Z = Scissors
total_score = {'A X': 4, 'A Y': 8, 'A Z': 3,
               'B X': 1, 'B Y': 5, 'B Z': 9,
               'C X': 7, 'C Y': 2, 'C Z': 6}
score = 0
for key in total_score.keys():
    score += data[key] * total_score[key]
print(f'Part 1:\nYour total score = {score}')

# Part 2
# You --> X = Lose, Y = Draw, Z = Win
total_score =    {'A X': 3, 'A Y': 4, 'A Z': 8,
                  'B X': 1, 'B Y': 5, 'B Z': 9,
                  'C X': 2, 'C Y': 6, 'C Z': 7}
score = 0
for key in total_score.keys():
    score += data[key] * total_score[key]
print(f'\nPart 2:\nYour total score = {score}')
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')