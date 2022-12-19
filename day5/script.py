"""Advent of code 2022 - Day 5"""
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
import re
import string

LETTER_PRIORITY = "." + string.ascii_lowercase + string.ascii_uppercase


def read_input(example=False):
    """
    Reads and parses the input file.
    """
    cwd = Path(__file__).parent
    filename = "example_input.txt" if example else "input.txt"

    data_file = (cwd / filename).with_suffix(".txt")

    with open(data_file, "r", encoding="utf-8") as file:
        stacks = defaultdict(list)
        instructions = []

        reading_stacks = True
        for line in file:
            if line.strip() == "":
                reading_stacks = False
                continue

            if reading_stacks:
                for i, b in enumerate(chunkstring(line, 4), start=1):
                    if b.strip() != "":
                        stacks[i].append(b.strip("[] \n"))
            else:
                # find first three numbers in a string
                instructions.append(list(map(int, re.findall(r"\d+", line))))

    for stack in stacks.keys():
        stacks[stack] = stacks[stack][::-1]

    return stacks, instructions


def execute_instructions(stacks, instructions, part2=False):
    """
    Carry out stacking instructions and returns the top items on each stack
    """
    for amount, origin, dest in instructions:
        if part2:
            stacks[dest].extend(stacks[origin][-amount:])
        else:
            stacks[dest].extend(reversed(stacks[origin][-amount:]))
        stacks[origin] = stacks[origin][:-amount]

    print(
        f"Part {2 if part2 else 1}: {''.join(stacks[key][-1] for key in sorted(stacks.keys()))}"
    )


def chunkstring(string, length):
    """Yield successive n-sized chunks from string."""
    return (string[0 + i : length + i] for i in range(0, len(string), length))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    execute_instructions(*read_input(args.example))
    execute_instructions(*read_input(args.example), part2=True)
