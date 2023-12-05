import re
def silver(puzzle_input):
    score = 0
    for line in puzzle_input:
        win_nums, g_nums = line.split(':')[1].split('|')
        win_nums = re.findall(r'\d+', win_nums)
        g_nums = re.findall(r'\d+', g_nums)
        num_matches = 0
        for num in win_nums:
            for num2 in g_nums:
                if num == num2:
                    num_matches += 1
        if num_matches > 0:
            score = score + 2 ** (num_matches - 1)
    print(f"Silver: {score}")

def gold(puzzle_input):
    score = 0
    card_amounts = {}
    for i, line in enumerate(puzzle_input):
        card_amounts[i + 1] = 1
 
    for line in puzzle_input:
        index = re.findall(r'\d+',  line.split(':')[0])[0]

        card_count = card_amounts[int(index)]

        win_nums, g_nums = line.split(':')[1].split('|')
        win_nums = re.findall(r'\d+', win_nums)
        g_nums = re.findall(r'\d+', g_nums)
        num_matches = 0
        for num in win_nums:
            for num2 in g_nums:
                if num == num2:
                    num_matches += 1
        if num_matches > 0:
            try:
                for i in range(num_matches):
                    card_amounts[int(index) + 1 + i] += card_count
            except:
                pass
    for i in card_amounts.values():
        score += i
    print(f"Gold: {score}")


def load_input():
    with open("input_small.txt") as puzzle_input:
        puzzle_input = puzzle_input.readlines()
        return puzzle_input

if __name__ == "__main__":
    with open("input.txt") as puzzle_input:
        puzzle_input = puzzle_input.readlines()
        silver(puzzle_input)
        gold(puzzle_input)