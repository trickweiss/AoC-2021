import re

EXPECTED_RESULT = 15
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def risk_level(x, y, heightmap):
    if x > 0 and heightmap[x][y] >= heightmap[x-1][y]:
        return 0
    if x < len(heightmap)-1 and heightmap[x][y] >= heightmap[x+1][y]:
        return 0
    if y > 0 and heightmap[x][y] >= heightmap[x][y-1]:
        return 0
    if y < len(heightmap[x])-1 and heightmap[x][y] >= heightmap[x][y+1]:
        return 0
    return int(heightmap[x][y]) + 1

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    sum = 0
    for x, line in enumerate(lines):
        for y, num in enumerate(line):
            sum += risk_level(x, y, lines)
    return sum

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
