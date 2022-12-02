"""Advent of code 2022 - Day 1"""
from argparse import ArgumentParser
from pathlib import Path


def read_input(example=False):
    """
    Reads a file with the same name as this script and returns the data as a list of lines.
    Adds _example to the filename if example is True.
    """
    cwd = Path(__file__).parent
    filename = "example_input.txt" if example else "input.txt"

    data_file = (cwd / filename).with_suffix(".txt")

    with open(data_file, "r", encoding="utf-8") as file:
        return file.read().splitlines()


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


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    data = read_input(args.example)
    calories = get_calories_per_elf(data)

    part1(calories)
    part2(calories)
