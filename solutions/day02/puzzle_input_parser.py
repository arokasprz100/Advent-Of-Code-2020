import re


def parse_puzzle_input(puzzle_input_to_parse):
    puzzle_input_to_parse = [re.split("[ -]", x) for x in puzzle_input_to_parse]
    return [(int(x[0]), int(x[1]), re.sub(':', '', x[2]), x[3]) for x in puzzle_input_to_parse]
