from argparse import ArgumentParser
from pathlib import Path

def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()

    return input

def get_calories_per_elf(data):
    elves = []
    calories = 0
    for line in data:
        if line:
            calories += int(line)
        else:
            elves.append(calories)
            calories = 0
    elves.append(calories)
    return elves

def part1(calories):
    print("Part 1")
    print(max(calories))

def part2(calories):
    print("Part 2")    
    print(sum(sorted(calories, reverse=True)[:3]))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    filename =  Path(__file__).stem
    if args.example:
        filename += '_example.txt'
    else:
        filename += '.txt'

    data = read_input(filename)
    calories = get_calories_per_elf(data)

    part1(calories)
    part2(calories)



