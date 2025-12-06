from get_input import get_input
from dotenv import load_dotenv

load_dotenv()

YEAR = 2025
DAY = 4

lines = get_input(YEAR, DAY).split("\n")

rows, cols = len(lines), len(lines[0])
total_rolls_accessed = 0

while True:
    rolls_accessed = 0
    rolls_indices = []

    for row in range(rows):
        for col in range(cols):
            if lines[row][col] != "@":
                continue
            
            rolls_count = 0
            for row_roll in (-1, 0, 1):
                for col_roll in (-1, 0, 1):
                    if rows > (row_roll + row) >= 0 and cols > (col_roll + col) >= 0:
                        if (row_roll + row) != row or (col_roll + col) != col:
                            if lines[row_roll + row][col_roll + col] == "@":
                                rolls_count += 1
                                    
            if rolls_count < 4:
                rolls_indices.append((row, col))
                rolls_accessed += 1
    
    total_rolls_accessed += rolls_accessed

    if rolls_accessed == 0:
        break

    for row, col in rolls_indices:
        line = lines[row]
        lines[row] = line[:col] + "x" + line[col+1:]

print(f"{total_rolls_accessed=}")