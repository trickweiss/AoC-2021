import sys
import re

EXPECTED_RESULT = 7
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    previous_measurement = sys.maxsize
    number_of_increases = 0
    with open(filename) as f:
        for line in f:
            current_measurement = int(line)
            if current_measurement > previous_measurement:
                number_of_increases += 1
            previous_measurement = current_measurement
    return number_of_increases

if puzzle(DEMO_FILE) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {puzzle(DEMO_FILE)} instead of {EXPECTED_RESULT}!')
