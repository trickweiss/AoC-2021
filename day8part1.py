import re

EXPECTED_RESULT = 26
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    num_seg_to_digit = {
        2: {1},
        3: {7},
        4: {4},
        5: {2, 3, 5},
        6: {0, 6, 9},
        7: {8},
    }
    with open(filename) as f:
        lines = f.readlines()
    lines = [re.split('\W+', line.rstrip()) for line in lines]
    count = 0
    for line in lines:
        for digit in line[-4:]:
            if len(num_seg_to_digit[len(digit)]) == 1:
                count += 1
    return count

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
