import time
# Advent of Code 2022 - Day 01 part 1 & 2
# https://adventofcode.com/2022/day/1
# Read input data

tic = time.perf_counter()
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1
# How many calories is the elf with the most calories carrying?
calories_per_elf = dict()
calories, elf = 0, 1

for line in lines:
    if line == '':
        calories_per_elf[elf] = calories
        elf += 1
        calories = 0
    else:
        calories += int(line)


print('Part 1:')
print(f'The elf with maximum calories carries {max(calories_per_elf.values())} calories')

# Part 2
# How many calories are the top 3 elfs with the most calories carrying?
list_of_calories = sorted(calories_per_elf.values(), reverse=True)[0:3]
print('\nPart 2:')
print(f'The top 3 elfs are carrying {sum(list_of_calories)} calories')
toc = time.perf_counter()

print(f'\nCalculation ended in {toc - tic:0.4f} seconds')