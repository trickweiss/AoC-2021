import re

EXPECTED_RESULT = 1134
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def get_nabos(coords, unsorted_coords):
    nabos = {coords}
    x = coords[0]
    y = coords[1]
    for a in range(2):
        if (x+1-2*a, y) in unsorted_coords:
            unsorted_coords.remove((x+1-2*a, y))
            nabos |= {(x+1-2*a, y)} | get_nabos((x+1-2*a, y), unsorted_coords)
        if (x, y+1-2*a) in unsorted_coords:
            unsorted_coords.remove((x, y+1-2*a))
            nabos |= {(x, y+1-2*a)} | get_nabos((x, y+1-2*a), unsorted_coords)
    return nabos

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    unsorted_coords = set()
    for x, line in enumerate(lines):
        for y, num in enumerate(line):
            if lines[x][y] != "9":
                unsorted_coords.add((x,y))
    basins = dict()
    basin = 0
    while len(unsorted_coords):
        coords = unsorted_coords.pop()
        basins[basin] = get_nabos(coords, unsorted_coords)
        basin += 1
    basin_sizes = [0] * len(basins)
    for i, basin in enumerate(basins):
        basin_sizes[i] = (len(basins[basin]))
    product = 1
    for size in sorted(basin_sizes)[-3:]:
        product *= size
    return product

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
