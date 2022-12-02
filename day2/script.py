"""Advent of code 2022 - Day 2"""
from argparse import ArgumentParser
from pathlib import Path


letter_to_hand = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
letter_to_win_condition = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

match_scores = {
    ("rock", "rock"): 3,
    ("rock", "paper"): 6,
    ("rock", "scissors"): 0,
    ("paper", "rock"): 0,
    ("paper", "paper"): 3,
    ("paper", "scissors"): 6,
    ("scissors", "rock"): 6,
    ("scissors", "paper"): 0,
    ("scissors", "scissors"): 3,
}


hand_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

hand_choices = {
    ("rock", "lose"): "scissors",
    ("rock", "draw"): "rock",
    ("rock", "win"): "paper",
    ("paper", "lose"): "rock",
    ("paper", "draw"): "paper",
    ("paper", "win"): "scissors",
    ("scissors", "lose"): "paper",
    ("scissors", "draw"): "scissors",
    ("scissors", "win"): "rock",
}


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
            hand_1, hand_2 = line.strip().split(" ")
            yield letter_to_hand[hand_1], hand_2


def part1(rounds):
    """Solution to part 1"""
    print("Part 1")
    score = 0
    for opponent, mine in rounds:
        hand = letter_to_hand[mine]
        score += match_scores[(opponent, hand)] + hand_score[hand]
    print(score)


def part2(rounds):
    """Solution to part 2"""
    print("Part 2")
    score = 0
    for opponent, mine in rounds:
        win_condition = letter_to_win_condition[mine]
        hand = hand_choices[(opponent, win_condition)]
        score += match_scores[(opponent, hand)] + hand_score[hand]
    print(score)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--example", action="store_true")
    args = parser.parse_args()

    data = list(read_input(args.example))
    part1(data)
    part2(data)
