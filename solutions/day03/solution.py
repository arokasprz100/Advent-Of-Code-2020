from functools import reduce
from solutions.common.file_reader import FileReader


def convert_to_int_array(to_convert):
    return [0 if x == '.' else 1 for x in to_convert]


def count_trees(vertical, horizontal, pattern):
    pattern_width = len(pattern[0])
    current_position = (vertical, horizontal)
    encountered_trees = 0
    while current_position[0] < len(pattern):
        encountered_trees = encountered_trees + puzzle_input[current_position[0]][current_position[1]]
        current_position = current_position[0] + vertical, (current_position[1] + horizontal) % pattern_width
    return encountered_trees


if __name__ == '__main__':
    puzzle_input = [convert_to_int_array(x) for x in FileReader.to_line_list("input.txt")]
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees = [count_trees(x[0], x[1], puzzle_input) for x in slopes]
    print("Part 1: {}".format(trees[1]))
    print("Part 2: {}".format(reduce(lambda x, y: x * y, trees)))
