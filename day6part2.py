import re

EXPECTED_RESULT = 26984457539
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    with open(filename) as f:
        line = list(map(int, re.split(',', f.readline().rstrip())))
    timers = [0] * 9
    for fish in line:
        timers[fish] += 1
    for day in range(256):
        timers.append(timers.pop(0))
        timers[6] += timers[8]
    return sum(timers)

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
