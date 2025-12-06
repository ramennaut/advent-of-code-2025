from get_input import get_input
from dotenv import load_dotenv

load_dotenv()

YEAR = 2025
DAY = 2

lines = get_input(YEAR, DAY).split(",")

ID_list = []

for line in lines:
    firstID, lastID = map(int, line.split("-"))

    for ID in range(firstID, lastID+1):
        strID = str(ID)
        i = (strID+strID).find(strID, 1, -1)
        if i != -1:
            ID_list.append(ID)

print(sum(ID_list))