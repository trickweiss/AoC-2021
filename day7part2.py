import re
import statistics
import math
import sys

EXPECTED_RESULT = 168
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    with open(filename) as f:
        line = list(map(int, re.split(',', f.readline().rstrip())))
        positions = [0] * (max(line) + 1)
        for crab in line:
            positions[crab] += 1
        poss1 = math.ceil(statistics.mean(line))
        poss2 = math.floor(statistics.mean(line))
        fuel = sys.maxsize
        for possibility in [poss1, poss2]:
            possible_fuel = 0
            for position, crab_count in enumerate(positions):
                if crab_count:
                    possible_fuel += crab_count * sum(range((abs(possibility - position)) + 1))
            if possible_fuel < fuel:
                fuel = possible_fuel
    return fuel

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
