import os
import urllib.request
from dotenv import load_dotenv
load_dotenv()

YEAR = 2025
DAY = 1

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

current_position = 50
count_part1 = 0
count_part2 = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])

    if distance > 99:
        count_part2 += distance // 100
    
    distance = distance % 100

    if direction == "L":
        if current_position != 0 and current_position <= distance:
            count_part2 += 1
        current_position = (current_position - distance) % 100
    else:
        if current_position != 0 and (100 - current_position) <= distance:
            count_part2 += 1
        current_position = (current_position + distance) % 100

    if current_position == 0:
        count_part1 += 1

print(f"Part 1 Password: {count_part1}")
print(f"Part 2 Password: {count_part2}")