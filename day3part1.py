import re

EXPECTED_RESULT = 198
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    gamma_rate = epsilon_rate = 0b0
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        num_lines = len(lines)
        for i, _ in enumerate(lines[0]): # all lines have the same length
            sum = 0
            for line in lines:
                sum += int(line[i])
            new_bit = sum > num_lines / 2
            gamma_rate = (gamma_rate << 1) + int(new_bit)
            epsilon_rate = (epsilon_rate << 1) + int(not new_bit)
    return int(gamma_rate * epsilon_rate)

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
