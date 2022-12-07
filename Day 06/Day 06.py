import time
from copy import deepcopy
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data

tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'

with open(file) as f:
    lines = f.read().splitlines()

string = lines[0]
# TESTCASES
# string = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'  # first marker after character 7, 19
# string = 'bvwbjplbgvbhsrlpgdmjqwftvncz'  # first marker after character 5, 23
# string = 'nppdvjthqldpwncqszvftbrmjlhg'  # first marker after character 6, 23
# string = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # first marker after character 10, 29
# string = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  # first marker after character 11, 26

# Part 1
length = 4
answer = length
for i in range(len(string)):
    sub_string = string[i: i + length]
    if len(frozenset(list(sub_string))) == length:
        break
    answer += 1
print(f'The answer to part 1 = {answer}')

# Part 2
length = 14
answer = length
for i in range(len(string)):
    sub_string = string[i: i + length]
    if len(frozenset(list(sub_string))) == length:
        break
    answer += 1
print(f'The answer to part 2 = {answer}')

toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
