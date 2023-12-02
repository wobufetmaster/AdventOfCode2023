from functools import reduce
import re

def number_map(matchobj):
    number_name_map = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    return number_name_map[matchobj.group(0)] + matchobj.group(0)[-1]

def replace_letters_with_numbers(line: str) -> str:
    subs = -1
    while subs != 0:
        new_str, subs = re.subn(r'one|two|three|four|five|six|seven|eight|nine', number_map, line)
        line = new_str
    return line

def calculate_line(line: str) -> int:
    nums = []
    for c in line:
        if c.isdigit():
            nums.append(c)
    return int(nums[0] + nums[-1])

def silver(puzzle_input):
    sum = 0
    for line in puzzle_input:
        sum = sum + calculate_line(line)
    print(f"Silver: {sum}")

def gold(puzzle_input):
    sum = 0
    for line in puzzle_input:
        sum = sum + calculate_line(replace_letters_with_numbers(line))
    print(f"Gold: {sum}")

if __name__ == "__main__":
    with open("input.txt") as puzzle_input:
        puzzle_input = puzzle_input.readlines()
        silver(puzzle_input)
        gold(puzzle_input)











