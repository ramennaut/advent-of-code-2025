import os
import urllib.request
from dotenv import load_dotenv
load_dotenv()

YEAR = 2025
DAY = 2

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

lines = file.strip().split(",")

ID_list = []

for line in lines:
    firstID, lastID = map(int, line.split("-"))

    for ID in range(firstID, lastID+1):
        strID = str(ID)
        i = (strID+strID).find(strID, 1, -1)
        if i != -1:
            ID_list.append(ID)

print(sum(ID_list))