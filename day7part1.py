import re
import statistics

EXPECTED_RESULT = 37
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    with open(filename) as f:
        line = list(map(int, re.split(',', f.readline().rstrip())))
        positions = [0] * (max(line) + 1)
        for crab in line:
            positions[crab] += 1
        fuel = 0
        best_pos = int(statistics.median(line))
        for position, crab_count in enumerate(positions):
            fuel += crab_count * abs(best_pos - position)
    return fuel

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
