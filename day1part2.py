import re
import sys

EXPECTED_RESULT = 5
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def window_sum(window):
    sum = 0
    for measurement in window:
        sum += measurement
    return sum

def puzzle(filename):
    prev_window = [sys.maxsize, sys.maxsize, sys.maxsize]
    number_of_increases = 0
    with open(filename) as f:
        for line in f:
            next_window = prev_window[1:]
            next_window.append(int(line))
            if window_sum(next_window) > window_sum(prev_window):
                number_of_increases += 1
            prev_window = next_window
    return number_of_increases

if puzzle(DEMO_FILE) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {puzzle(DEMO_FILE)} instead of {EXPECTED_RESULT}!')
