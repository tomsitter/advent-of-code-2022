"""Advent of code 2022 - Day 3"""
from argparse import ArgumentParser
from pathlib import Path
import string

LETTER_PRIORITY = "." + string.ascii_lowercase + string.ascii_uppercase


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


def part1(data):
    """
    Finds overlapping characters in the rucksacks and returns the sum of priorities of each item
    """
    rucksacks = [
        (set(pack[: len(pack) // 2]), set(pack[len(pack) // 2 :])) for pack in data
    ]
    priority = 0
    for cmp1, cmp2 in rucksacks:
        overlapping_char = cmp1.intersection(cmp2)
        priority += LETTER_PRIORITY.index(overlapping_char.pop())
    print(f"Part 1: {priority}")


def part2(data):
    """
    Finds overlapping characters in group of 3 rucksacks and returns the sum of priorities of each item
    """
    groups = [list(map(set, data[i : i + 3])) for i in range(0, len(data), 3)]
    priority = 0
    for cmp1, cmp2, cmp3 in groups:
        overlapping_char = cmp1.intersection(cmp2, cmp3)
        priority += LETTER_PRIORITY.index(overlapping_char.pop())
    print(f"Part 2: {priority}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    data = read_input(args.example)

    part1(data)
    part2(data)
