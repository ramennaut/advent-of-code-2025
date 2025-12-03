import os
import urllib.request
from dotenv import load_dotenv
load_dotenv()

YEAR = 2025
DAY = 3

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

digits = int(input("Enter the number of batteries to turn on: "))

joltage_list = []
for line in lines:

    num_list = []
    for i in range(len(line)):
        num = int(line[i])
        num_list.append(num)

    joltage_values = []
    num_to_remove = len(num_list) - digits
    
    for num in num_list:
        while num_to_remove > 0 and joltage_values and joltage_values[-1] < num:
            joltage_values.pop()
            num_to_remove -= 1
        joltage_values.append(num)

    if num_to_remove > 0:
        joltage_values = joltage_values[:-num_to_remove]
    
    joltage = "".join(str(value) for value in joltage_values) 
    joltage_list.append(int(joltage))

print(f"Joltage List: {joltage_list}")
print(f"Total Output Joltage: {sum(joltage_list)}")
