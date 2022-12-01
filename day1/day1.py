from argparse import ArgumentParser
from pathlib import Path


def get_data(example=False):
    """
    Reads a file with the same name as this script and returns the data as a list of lines.
    Adds _example to the filename if example is True.
    """
    cwd = Path(__file__).parent
    filename =  Path(__file__).stem + "_example" if example else Path(__file__).stem

    data_file = (cwd / filename).with_suffix('.txt')

    with open(data_file) as f:
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

    data = get_data(args.example)
    calories = get_calories_per_elf(data)

    part1(calories)
    part2(calories)



