import itertools


grid = None

def symbol_adjacent(x, y):
    def g(x,y):
        try:
            retval = not grid[x][y].isdigit() and grid[x][y] != '.' and grid[x][y] != '\n' 
            return retval
        except:
            return False
    return g(x-1, y + 1) or g(x, y+1) or g(x + 1, y+1) or g(x+1, y) or g(x+1, y - 1) or g(x, y - 1) or g(x-1, y-1) or g(x-1, y)

def silver(puzzle_input):
    sum = 0
    cur_number = ""
    should_add_number = False
    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
 
            if not c.isdigit():
                if not should_add_number:
                    cur_number = ""
                else:
                    sum = sum + int(cur_number)
                    cur_number = ""
                    should_add_number = False

            if c.isdigit():
                cur_number = cur_number + c
                if symbol_adjacent(i, j):
                    should_add_number = True

    print(f"Silver: {sum}")

def gear_adjacent(x,y):
    def g(x,y):
        try:
            if grid[x][y] == '*':
                return (x,y)
            return None
        except:
            return None
    return g(x-1, y + 1) or g(x, y+1) or g(x + 1, y+1) or g(x+1, y) or g(x+1, y - 1) or g(x, y - 1) or g(x-1, y-1) or g(x-1, y)

def gold(puzzle_input):
    gear_info = {}
    cur_number = ""
    gear_position = None

    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
            if c == "*":
                gear_info[(i,j)] = {'count': 0, 'product': 1}

    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
            if not c.isdigit():
                if not gear_position:
                    cur_number = ""
                else:
                    gear_info[gear_position]['count'] += 1
                    gear_info[gear_position]['product'] *= int(cur_number)
                    cur_number = ""
                    gear_position = None

            if c.isdigit():
                cur_number = cur_number + c
                if not gear_position:
                    gear_position = gear_adjacent(i, j)
    sum = 0
    for info in gear_info.values():
        if info['count'] == 2:
            sum += info['product']
    print(f"Gold: {sum}")

if __name__ == "__main__":
    with open("input.txt") as puzzle_input:
        puzzle_input = puzzle_input.readlines()
        grid = puzzle_input
        silver(puzzle_input)
        gold(puzzle_input)