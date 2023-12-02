import re

def line_is_valid(line: str) -> bool:
    ball_amounts = {'red': 12, 'green': 13, 'blue': 14}
    amounts = re.findall(r'(\d+) (\w+)', line)
    for number, color in amounts:
        if ball_amounts[color] < int(number):
            return False
    return True

def minimum_cubes(line: str) -> int:
    amounts = re.findall(r'(\d+) (\w+)', line)
    current_minimum = {'red': 0, 'green': 0, 'blue': 0}
    for number, color in amounts:
        if current_minimum[color] < int(number):
            current_minimum[color] = int(number)
    return current_minimum['red'] * current_minimum['green'] * current_minimum['blue']

def silver(puzzle_input):
    i = 1
    sum = 0
    for line in puzzle_input:
        if line_is_valid(line):
            sum = sum + i
        i = i + 1
    print(f"Silver: {sum}")

def gold(puzzle_input):
    sum = 0
    for line in puzzle_input:
        sum = sum + minimum_cubes(line)
    print(f"Gold: {sum}")

if __name__ == "__main__":
    with open("input.txt") as puzzle_input:
        puzzle_input = puzzle_input.readlines()
        silver(puzzle_input)
        gold(puzzle_input)