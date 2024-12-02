# Advent of Code 2024
# Day 2. Red-Nosed Reports

# 1. Find the total number of reports that are "safe". 
file_path = "sample.txt"
file_path = "input.txt"

reports = []
with open(file_path) as file:
    for line in file:
        reports.append([int(num) for num in line.split()])

def is_valid(report):
    return (
        (all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:]))) and
        all(1 <= abs(i - j) <= 3 for i, j in zip(report, report[1:]))
    )

print(sum(list(map(is_valid, reports))))

# 2. Allow the total number of "safe" reports to tolerate a single bad value.
# num_safe = 0

# num_safe = 0
# for report in reports:
#     valid_found = False
#     for i in range(len(report) + 1):
#         subsequence = report[:i] + report[i+1:]
#         if is_valid(subsequence):
#             valid_found = True
#             break
#     if valid_found == True:
#         num_safe += 1
# print(num_safe)

# eh, this is better than my above solution
print(sum(map(lambda level: any(is_valid(level[:i] + level[i+1:]) for i in range(len(level)+1)), reports)))
