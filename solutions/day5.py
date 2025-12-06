from get_input import get_input
from dotenv import load_dotenv

load_dotenv()

YEAR = 2025
DAY = 5

lines = get_input(YEAR, DAY).split("\n")

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