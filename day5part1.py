import re

EXPECTED_RESULT = 5
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def find_points(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    points = set()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points.add((x, y))
    return points

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [list(map(int, re.split('\D+', line.rstrip()))) for line in lines]
    prev_points = set()
    danger_points = set()
    for line in lines:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        if x1 == x2 or y1 == y2:
            points = find_points(x1, y1, x2, y2)
            danger_points |= (prev_points & points)
            prev_points |= points
    return len(danger_points)

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
