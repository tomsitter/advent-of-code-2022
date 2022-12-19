"""Advent of code 2022 - Day 6"""
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
        data = file.read().strip()
        for char in data:
            yield char


def find_end_of_marker(data, marker_length):
    """
    Finds a the first set of 4 unique characters and returns the index of the last character indexed at 1
    """
    for i in range(len(data) - marker_length - 1):
        if len(set(data[i : i + marker_length])) == marker_length:
            print(f"Marker found at: {i + marker_length}")
            return


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    data = list(read_input(args.example))

    find_end_of_marker(data, marker_length=4)
    find_end_of_marker(data, marker_length=14)
