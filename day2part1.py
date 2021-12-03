import re

EXPECTED_RESULT = 150
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    horizontal_position = 0
    depth = 0
    with open(filename) as f:
        for line in f:
            command, _, units = line.partition(' ')
            if command == "forward":
                horizontal_position += int(units)
            elif command == "down":
                depth += int(units)
            elif command == "up":
                depth -= int(units)
            else:
                print("WTF")
                return 0
    return horizontal_position * depth

if puzzle(DEMO_FILE) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {puzzle(DEMO_FILE)} instead of {EXPECTED_RESULT}!')
