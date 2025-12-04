import os
import urllib.request
from dotenv import load_dotenv
load_dotenv()

YEAR = 2025
DAY = 4

url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
session_cookie = os.getenv("AOC_SESSION")
email = os.getenv("AOC_USER_AGENT_EMAIL", "example@example.com")

if not session_cookie:
    raise ValueError("AOC_SESSION is missing.")

req = urllib.request.Request(
    url,
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": f"github.com/ramennaut/advent-of-code-2025 by {email}",
    },
)

with urllib.request.urlopen(req) as response:
    file = response.read().decode("utf-8")

lines = file.strip().split("\n")

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