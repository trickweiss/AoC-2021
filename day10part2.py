import re
from collections import deque

EXPECTED_RESULT = 288957
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    chunk_opener = {'(': ')', '[': ']', '{': '}', '<': '>'}
    chunk_closer = { ')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in lines:
        stack = deque()
        for char in line:
            if char in chunk_opener:
                stack.append(char)
            elif char in chunk_closer and len(stack):
                if char != chunk_opener[stack.pop()]:
                    stack.clear()
                    break
        stack.reverse()
        score = 0
        for char in stack:
            score *= 5
            score += chunk_closer[chunk_opener[char]]
        if score:
            scores.append(score)
    return sorted(scores)[int(len(scores)/2)]

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
