from get_input import get_input
from dotenv import load_dotenv

load_dotenv()

YEAR = 2025
DAY = 3

lines = get_input(YEAR, DAY).split("\n")

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
