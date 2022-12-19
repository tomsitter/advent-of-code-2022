"""Advent of code 2022 - Day 4"""
from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Section:
    start: int
    end: int

    def contains(self, other: Section):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: Section):
        return (
            self.start <= other.start <= self.end or self.start <= other.end <= self.end
        )


def read_input(example=False):
    """
    Reads a file with the same name as this script and returns the data as a list of lines.
    Adds _example to the filename if example is True.
    """
    cwd = Path(__file__).parent
    filename = "example_input.txt" if example else "input.txt"

    data_file = (cwd / filename).with_suffix(".txt")

    with open(data_file, "r", encoding="utf-8") as file:
        for line in file:
            s1, s2 = line.strip().split(",")

            yield (Section(*map(int, s1.split("-"))), Section(*map(int, s2.split("-"))))


def part1(sections):
    """Solution to part 1"""
    print("Part 1")
    matches = 0
    for s1, s2 in sections:
        if s1.contains(s2) or s2.contains(s1):
            matches += 1
    print(matches)


def part2(sections):
    """Solution to part 2"""
    print("Part 2")
    matches = 0
    for s1, s2 in sections:
        if s1.overlaps(s2) or s2.overlaps(s1):
            matches += 1
    print(matches)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    data = list(read_input(args.example))
    part1(data)
    part2(data)
