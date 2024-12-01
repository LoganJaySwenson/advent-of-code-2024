# Advent of Code 2024
# Day 1. Historian Hysteria

# 1. Pair the smallest, second-smallest, third-smallest numbers, etc. in two lists and find the sum of all differences. 
file_path = "sample.txt"
file_path = "input.txt"

left = []
right = []
with open(file_path) as file:
    for line in file:
        left.append(int(line.strip().split()[0]))
        right.append(int(line.strip().split()[-1]))
left.sort()
right.sort()

differences = []
for num1, num2 in zip(left, right):
    differences.append(abs(num1 - num2))
sum(differences)

# 2. Count the number of times each value appears in the two lists and calculate a total similarity score.
similarity_score = []
for i in left:
    num_occurences = right.count(i)
    similarity_score.append(i * num_occurences)
sum(similarity_score)


