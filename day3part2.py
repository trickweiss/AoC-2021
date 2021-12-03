import re

EXPECTED_RESULT = 230
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def most_common_bit(lines, position):
    sum = 0
    for line in lines:
        sum += int(line[position])
    return int (sum >= len(lines) / 2)

def criterion_fitters(lines, position, is_ogr):
    new_list = []
    mcb = most_common_bit(lines, position)
    for line in lines:
        if (int(line[position]) == mcb) == is_ogr:
            new_list.append(line)
    return new_list

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        oxygen_generator_rating = lines
        co2_scrubber_rating = lines
        position = 0
        while len(oxygen_generator_rating) > 1:
            oxygen_generator_rating = criterion_fitters(oxygen_generator_rating, position, True)
            position += 1
        position = 0
        while len(co2_scrubber_rating) > 1:
            co2_scrubber_rating = criterion_fitters(co2_scrubber_rating, position, False)
            position += 1
    return int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
