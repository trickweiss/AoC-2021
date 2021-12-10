import re
from collections import deque

EXPECTED_RESULT = 26397
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    chunk_opener = {'(': ')', '[': ']', '{': '}', '<': '>'}
    chunk_closer = { ')': 3, ']': 57, '}': 1197, '>': 25137}
    illegals = {')': 0, ']': 0, '}': 0, '>': 0}
    for line in lines:
        stack = deque()
        for char in line:
            if char in chunk_opener:
                stack.append(char)
            elif char in chunk_closer and len(stack):
                if char != chunk_opener[stack.pop()]:
                    illegals[char] += 1
                    break
    score = 0
    for char in illegals:
        score += illegals[char] * chunk_closer[char]
    return score

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
