import os
import urllib.request
from dotenv import load_dotenv
load_dotenv()

YEAR = 2025
DAY = 5

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

separator_index = lines.index("")
input_ranges = [tuple(map(int,ranges.split("-")))for ranges in lines[:separator_index]]
availableIDs = list(map(int, lines[separator_index+1:]))

count = sum(
    any(startingID <= x <= endingID for startingID, endingID in input_ranges)
    for x in availableIDs
)

input_ranges.sort()
merged_ranges = []

for startingID, endingID in input_ranges:
    if merged_ranges and startingID <= merged_ranges[-1][1]:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], endingID)
    else:
        merged_ranges.append([startingID, endingID])

freshIDs = sum(endingID - startingID + 1 for startingID, endingID in merged_ranges)

print(f"{count=}")
print(f"{freshIDs=}")