from get_input import get_input
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

YEAR = 2025
DAY = 7

lines = get_input(YEAR, DAY).split("\n")

height, width = len(lines), len(lines[0])

start_row = start_col = None
for row in range(height):
    for col in range(width):
        if lines[row][col] == "S":
            start_row, start_col = row, col
            break
    if start_row is not None:
        break

active_state = {start_col}
splits = 0

for row in range(start_row + 1, height):
    next_state = set()
    for col in active_state:
        if lines[row][col] == "^":
            splits += 1
            if col - 1 >= 0:
                next_state.add(col - 1)
            if col + 1 < width:
                next_state.add(col + 1)
        else:
            next_state.add(col)
    active_state = next_state

print(splits)

paths = Counter({start_col: 1})

for row in range(start_row + 1, height):
    next_path = Counter()
    for col, npaths in paths.items():
        if lines[row][col] == "^":
            if col - 1 >= 0:
                next_path[col - 1] += npaths
            if col + 1 < width:
                next_path[col + 1] += npaths
        else:
            next_path[col] += npaths
    paths = next_path

timelines = sum(paths.values())
print(timelines)
