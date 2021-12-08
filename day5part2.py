import re

EXPECTED_RESULT = 12
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def find_points(x1, y1, x2, y2):
    stepx = 1
    stepy = 1
    if x1 > x2:
        stepx = -1
    if y1 > y2:
        stepy = -1
    points = set()
    xs = range(x1, x2 + stepx, stepx)
    ys = range(y1, y2 + stepy, stepy)
    if len(ys) == len(xs):
        for i, x in enumerate(xs):
            points.add((x, ys[i]))
    elif len(ys) < len(xs):
        for x in xs:
            points.add((x, ys[0]))
    else:
        for y in ys:
            points.add((xs[0], y))
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
        points = find_points(x1, y1, x2, y2)
        danger_points |= (prev_points & points)
        prev_points |= points
    return len(danger_points)

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
