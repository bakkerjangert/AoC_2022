import time
import math
import sys

# Advent of Code 2022 - Day 10 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

def main_loop(start_point=None):
    def get_target_nodes(node):
        target_nodes = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x, y = node[0] + dx, node[1] + dy
                # skip if target_node not in grid or target_node == node
                if not 0 <= x < len(lines[0]) or not 0 <= y < len(lines) or node == (x, y):
                    continue
                # skip diagonals
                if dx != 0 and dy != 0:
                    continue
                val_a, val_b = lines[node[1]][node[0]], lines[y][x]
                if height_tabel[val_b] <= height_tabel[val_a] + 1 and (x, y) in dormant_nodes:
                    target_nodes.append((x, y))
        return target_nodes


    def sort_active_nodes():
        active_nodes.sort(key=lambda x: x[1])

    file = 'input.txt'
    # file = 'test.txt'
    with open(file) as f:
        lines = f.read().splitlines()

    height_tabel = dict()
    letter_score = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        height_tabel[letter] = letter_score
        letter_score += 1

    dormant_nodes = []  # List of tuples --> [(x, y), (x, y), ... (x, y)]
    active_nodes = []  # List of lists --> [[(x, y), score, [(x_t1, y_t1), (x_t2, y_t2), ...]], [...], ...]
    finished_nodes = dict()  # {(x, y): min_score, (x, y): min_score ... }

    for x in range(len(lines[0])):
        for y in range(len(lines)):
            dormant_nodes.append((x, y))

    start_node, end_node = start_point, None
    for y, line in enumerate(lines):
        if 'S' in line:
            x = line.index('S')
            if start_node is None:
                start_node = (x, y)
            lines[y] = lines[y][:x] + 'a' + lines[y][x + 1:]
        if 'E' in line:
            x = line.index('E')
            end_node = (x, y)
            lines[y] = lines[y][:x] + 'z' + lines[y][x + 1:]

    target_start = get_target_nodes(start_node)
    # print(target_start)
    active_nodes.append([start_node, 0, target_start])
    dormant_nodes.remove(start_node)
    # print(active_nodes)

    while len(active_nodes) > 0:
        sort_active_nodes()
        current_node = active_nodes.pop(0)
        score = current_node[1]
        if len(current_node[2]) == 0:
            if current_node[0] not in finished_nodes.keys():
                finished_nodes[current_node[0]] = score
            elif finished_nodes[current_node[0]] > score:
                finished_nodes[current_node[0]] = score
            continue
        next_node = current_node[2].pop(0)
        # print(f'analysing {next_node}')
        active_nodes.append(current_node)
        active_node_list = [i[0] for i in active_nodes]
        # print(active_node_list)
        if next_node in active_node_list:
            for i, node in enumerate(active_nodes):
                if next_node == node[0]:
                    index = i
            if active_nodes[index][1] > score + 1:
                active_nodes[index][1] = score + 1
            continue
        elif next_node in finished_nodes.keys():
            if finished_nodes[next_node] > score + 1:
                finished_nodes[next_node] = score + 1
            continue
        else:
            target_nodes = get_target_nodes(next_node)
            dormant_nodes.remove(next_node)
            active_nodes.append([next_node, score + 1, target_nodes])

    # for y in range(len(lines)):
    #     for x in range(len(lines[0])):
    #         try:
    #             score = str(finished_nodes[(x, y)])
    #         except KeyError:
    #             score = '###'
    #         if len(score) < 2:
    #             score = '0' + score
    #         if len(score) < 3:
    #             score = '0' + score
    #         print(score, end=' ')
    #     print('')
    if end_node in finished_nodes:
        return finished_nodes[end_node]
    else:
        return len(lines) * len(lines[0])

print(f'The answer to part 1 = {main_loop()}')

file = 'input.txt'
# file = 'test.txt'
with open(file) as f:
    lines = f.read().splitlines()

min_length = len(lines) * len(lines[0])
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'a':
            val = main_loop((x, y))
            min_length = min(min_length, val)
            print(f'Found trail at {(x, y)} with length {val}')
print(f'The answer to part 2 = {min_length}')


# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')

