import re

EXPECTED_RESULT = 1924
BASE_NAME = re.search('day[0-9]+', __file__)[0]
DEMO_FILE = f"{BASE_NAME}demo.txt"
PUZZLE_FILE = f"{BASE_NAME}input.txt"

def score(card, calls_so_far, call):
    cardset = set()
    for i in range(0,5):
        cardset = cardset | set(card[i])
    return sum(list(map(int, cardset - calls_so_far))) * int(call)

def solve_card(card, calls):
    for i, call in enumerate(calls):
        calls_so_far = set(calls[:i+1])
        for row in range(0, 5):
            if set(card[row]) | calls_so_far == calls_so_far:
                return i, score(card, calls_so_far, calls[i])
        for col in range(0, 5):
            if {row[col] for row in card} | calls_so_far == calls_so_far:
                return i, score(card, calls_so_far, calls[i])
    return 0, 0 # card never solves

def puzzle(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    calls = lines[0].split(',')
    cards = []
    card = []
    for line in lines[1:]:
        if (l := line.split()):
            card.append(l)
        if len(card) == 5:
            cards.append(card)
            card = []
    max_steps = 0
    winning_score = 0
    for card in cards:
        steps, score = solve_card(card, calls)
        if steps > max_steps:
            max_steps = steps
            winning_score = score
    return winning_score

if (d := puzzle(DEMO_FILE)) == EXPECTED_RESULT:
    print(puzzle(PUZZLE_FILE))
else:
    print(f'Oh no! Your demo got {d} instead of {EXPECTED_RESULT}!')
