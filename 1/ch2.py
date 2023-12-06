from ch1 import problem

import re


conversion_table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

regex = '(' + '|'.join([key for key in conversion_table.keys()]) + ')'

weird_lines = []

def solve_line(line):
    found_numbers = re.findall(regex, line)
    if found_numbers:
        return int(conversion_table[found_numbers[0]] + conversion_table[found_numbers[-1]])
    weird_lines.append(line)
    return 0

solution = 0
for line in problem:
    print(line)
    this_line_solved = solve_line(line)
    print(this_line_solved)
    solution += this_line_solved
    print(solution)
    
print(solution)

print("Weird lines:")
print(weird_lines)
    
    
    
    