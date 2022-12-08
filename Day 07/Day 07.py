import time
from copy import deepcopy
# Advent of Code 2022 - Day 05 part 1 & 2
# https://adventofcode.com/2022/day/5
# Read input data

tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'
file = 'aoc_2022_day07_deep.txt'

with open(file) as f:
    lines = f.read().splitlines()


class Directory:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.sub_dirs = dict()  # name + total size
        self.files = dict()  # name + total size
        self.total_size = None

    def add_sub_dir(self, name):
        self.sub_dirs[name] = None  # not know size

    def add_file(self, name, size):
        self.files[name] = size

    def calculate_size(self):
        if None in self.sub_dirs.values():
            pass
        else:
            self.total_size = sum(self.sub_dirs.values()) + sum(self.files.values())

directories = dict()
cur_dir = []
max_level = 0
max_size = 100_000
answer = 0
no_lines = len(lines)

for i, line in enumerate(lines):
    if i % 10000 == 0:
        print(f'At {round(i / no_lines * 100, 2)}%')
    if '$ cd' in line:
        if '..' in line:
            cur_dir.pop(-1)
        elif '/' in line and '/' in directories.keys():
            cur_dir = ['/']
        else:
            dir_name = line.split(' ')[-1]
            cur_dir.append(dir_name)
            dir_name = '/'.join(cur_dir)
            if len(cur_dir) > 1:
                prev_dir = '/'.join(cur_dir[:-1])
                directories[prev_dir].add_sub_dir(dir_name)
            if dir_name not in directories.keys():
                directories[dir_name] = Directory(dir_name, len(cur_dir))
                max_level = max(max_level, len(cur_dir))
    elif line[:3] == 'dir':
        pass
    elif line == '$ ls' or line == '':
        pass
    else:
        file_name = line.split(' ')[-1]
        file_size = int(line.split(' ')[0])
        dir_name = '/'.join(cur_dir)
        directories[dir_name].add_file(file_name, file_size)

for level in range(max_level, 0, -1):
    for directory in directories.values():
        if directory.level == level:
            # print(f'Calculating total size of {directory.name}')
            for sub_dir in directory.sub_dirs.keys():
                directory.sub_dirs[sub_dir] = directories[sub_dir].total_size
            directory.calculate_size()
            if directory.total_size is None:
                print('Warning --> Total size not calculated')
            if directory.total_size <= max_size:
                answer += directory.total_size

print(f'The answer to part 1 = {answer}')

disk_size = 70_000_000
required_size = 30_000_000
to_delete = required_size - (disk_size - directories['/'].total_size)

min_delta = disk_size
answer = 0
for directory in directories.values():
    if directory.total_size > to_delete:
        delta = directory.total_size - to_delete
        if delta < min_delta:
            min_delta = delta
            answer = directory.total_size

print(f'The answer to part 2 = {answer}')

toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
