# %%
from math import prod
from get_input import get_input
from dotenv import load_dotenv

load_dotenv()

YEAR = 2025
DAY = 6

lines = get_input(YEAR, DAY).split("\n")

operations = lines[-1].split()
num_list = [list(lines[i]) for i in range(len(lines)-1)]
num_list_transposed = list(map(list, zip(*num_list)))
max_len = len(num_list_transposed[0])
separator = [" "] * max_len

num_list_grouped = []
current = []
for row in num_list_transposed:
    if row == separator:
        current and num_list_grouped.append(current)
        current = []
    else:
        current.append(row)

current and num_list_grouped.append(current)

num_list_digits = [
    [[digit if digit != " " else "" for digit in group] for group in row]
    for row in num_list_grouped
]

results = []
for i in range(len(num_list_digits)):
    current = []
    for group in num_list_digits[i]:
        digit = int("".join(group))
        current.append(digit)
    if operations[i] == "+":
        results.append(sum(current))
    else:
        results.append(prod(current))

print(f"Password: {sum(results)}")