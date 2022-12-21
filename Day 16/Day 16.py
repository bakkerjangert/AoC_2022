import time
import numpy as np
# Advent of Code 2022 - Day 15 part 1 & 2
# https://adventofcode.com/2022/day/10

# Start time
tic = time.perf_counter()

file = 'input.txt'
# file = 'test.txt'


with open(file) as f:
    lines = f.read().splitlines()


class Valve:
    def __init__(self, string):
        self.name = string.split('ve ')[1].split(' ')[0]
        self.flow_rate = int(string.split(';')[0].split('=')[1])
        if 'valves' in string:
            self.goals = string.split('valves ')[-1].split(', ')
        else:
            self.goals = string.split('valve ')[-1].split(', ')

    def __repr__(self):
        return f'Valve {self.name} has flow rate {self.flow_rate} and leads to {self.goals}'


def remaining_score(minute, flow_rates):
    new_score = 0
    for rate in sorted(flow_rates, reverse=True):
        new_score += rate * max(minute, 0)
        minute -= 2  # Do a step and open
    return new_score


def remaining_score_pt2(minute, flow_rates):
    new_score = 0
    flow_rates = sorted(list(flow_rates))
    while len(flow_rates) > 0:
        new_score += flow_rates.pop(0) * max(minute, 0)
        if len(flow_rates) > 0:
            new_score += flow_rates.pop(0) * max(minute, 0)
        minute -= 2  # Do a step and open
    return new_score


flow_rates = []
valves = dict()
for line in lines:
    valve = line.split()[1]
    valves[valve] = Valve(line)
    if valves[valve].flow_rate > 0:
        valves[valve].goals.append('OPEN')
        flow_rates.append(valves[valve].flow_rate)

paths = set()
start_point = (0, tuple(flow_rates), tuple(), ('My Path', 'AA',))
paths.add(start_point)
print(paths)

max_score = 0
for minute in range(29, 0, -1):
    print(f'Analysing minute {minute}')
    new_paths = set()
    for path in paths:
        valve = path[3][-1] if path[3][-1] != 'OPEN' else path[3][-2]
        for goal in valves[valve].goals:
            if goal == path[3][-2]:
                continue  # Do not return before opening
            elif goal == 'OPEN' and valve in path[2]:
                continue  # Valve already open
            elif goal == 'OPEN':
                score = path[0] + minute * valves[valve].flow_rate
                max_score = max(score, max_score)
                remaining_flow_rates = list(path[1])
                remaining_flow_rates.remove(valves[valve].flow_rate)
                remaining_flow_rates = tuple(remaining_flow_rates)
                open_valves = path[2] + (valve,)
            else:
                score = path[0]
                remaining_flow_rates = path[1]
                open_valves = path[2]
            max_path_score = remaining_score(minute - 1, remaining_flow_rates)
            if score + max_path_score >= max_score:
                new_path = (score, remaining_flow_rates, open_valves, path[3] + (goal,))
                new_paths.add(new_path)
                # print(new_path)
    # print(f'\nMinute {30 - minute}:')
    # for path in sorted(new_paths):
    #     print(path)
    # input(f'Minute {30 - minute} finished')
    paths = new_paths
print(max_score)
print(sorted(list(paths))[-1])


# Part 2
paths = set()
start_point = (0, tuple(flow_rates), tuple(), ('My Path', 'AA',), ('Elephant', 'AA'))
print(f'Start part 2 = {start_point}')
paths.add(start_point)

max_score = 0
for minute in range(25, 0, -1):
    print(f'Analysing minute {minute}')
    new_paths = set()
    for path in paths:
        my_valve = path[3][-1] if path[3][-1] != 'OPEN' else path[3][-2]
        el_valve = path[4][-1] if path[4][-1] != 'OPEN' else path[4][-2]
        for my_goal in valves[my_valve].goals:
            if my_goal == path[3][-2]:
                continue  # Do not return before opening
            elif my_goal == 'OPEN' and my_valve in path[2]:
                continue  # Valve already open
            elif my_goal == 'OPEN':
                # print('HERE??')
                score = path[0] + minute * valves[my_valve].flow_rate
                max_score = max(score, max_score)
                remaining_flow_rates = list(path[1])
                remaining_flow_rates.remove(valves[my_valve].flow_rate)
                remaining_flow_rates = tuple(remaining_flow_rates)
                open_valves = path[2] + (my_valve,)
            else:
                score = path[0]
                remaining_flow_rates = path[1]
                open_valves = path[2]
            # Elephant
            for el_goal in valves[el_valve].goals:
                if el_goal == path[4][-2]:
                    continue  # Do not return before opening
                elif el_goal == 'OPEN' and el_valve in open_valves:
                    continue  # Valve already open
                elif el_goal == 'OPEN':
                    # Use values from my path!
                    score += minute * valves[el_valve].flow_rate
                    max_score = max(score, max_score)
                    remaining_flow_rates = list(remaining_flow_rates)
                    remaining_flow_rates.remove(valves[el_valve].flow_rate)
                    remaining_flow_rates = tuple(remaining_flow_rates)
                    open_valves = open_valves + (el_valve,)
                else:
                    pass  # Do not overwrite my_path values!
                max_path_score = remaining_score(minute - 1, remaining_flow_rates)
                if score + max_path_score >= max_score:
                    new_path = (score, remaining_flow_rates, open_valves, path[3] + (my_goal,), path[4] + (el_goal,))
                    # print(new_path)
                    new_paths.add(new_path)
    paths = new_paths
print(max_score)
print(sorted(list(paths))[-1])

# for key in sorted(valves.keys()):
#     print(valves[key])


# End and calculation time
toc = time.perf_counter()
print(f'\nCalculation ended in {toc - tic:0.4f} seconds')
