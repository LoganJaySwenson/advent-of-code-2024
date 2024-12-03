# Advent of Code 2024
# Day 3. Mull It Over

import re

# 1. Find all occurences of "mul(X,Y)" and calculate the sum of each X*Y pair. 
file_path = "sample.txt"
file_path = "input.txt"

with open(file_path) as file:
    data = file.read()

pattern = r"mul\((\d+),(\d+)\)"
total = 0
for num1, num2 in re.findall(pattern, data):
    total += int(num1) * int(num2)
print(total)

# 2. Same as before, but the "do()" and "don't()" instructions enable/disable "mul()" operations.
pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
flag = True
total = 0
for num1, num2, do, dont in re.findall(pattern, data):
    if do == "do()":
        flag = True 
    elif dont == "don't()":
        flag = False 
    elif num1 and num2:
        total += int(num1) * int(num2) * flag 
print(total)
