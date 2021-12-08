import re

EXPECTED_RESULT = 61229
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def output_value(signals):
    num_seg_to_digit = {
        2: {1},
        3: {7},
        4: {4},
        5: {2, 3, 5},
        6: {0, 6, 9},
        7: {8},
    }
    codes = dict.fromkeys(set(signals), -1)
    digits = [''] * 10
    for code in codes:
        num_segs = len(code)
        if len(num_seg_to_digit[num_segs]) == 1:
            codes[code] = min(num_seg_to_digit[num_segs])
            digits[min(num_seg_to_digit[num_segs])] = code
    for code in codes:
        num_segs = len(code)
        if num_segs == 5: # 3 does include 7, 5 has 3 segs in common with 4
            if len(set(digits[7])&set(code)) == 3:
                codes[code] = 3
                digits[3] = code
            elif len(set(digits[4])&set(code)) == 3:
                codes[code] = 5
                digits[5] = code
            else:
                codes[code] = 2
                digits[2] = code
        elif num_segs == 6: # 6 does not include 7, 9 does include 4
            if len(set(digits[4])&set(code)) == 4:
                codes[code] = 9
                digits[9] = code
            elif len(set(digits[7])&set(code)) == 3:
                codes[code] = 0
                digits[0] = code
            else:
                codes[code] = 6
                digits[6] = code
    value = 0
    for signal in signals[-4:]:
        value += codes[signal]
        value *= 10
    return int(value / 10)

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [re.split('\W+', line.rstrip()) for line in lines]
    sum = 0
    for line in lines:
        sum += output_value(line)
    return sum

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
