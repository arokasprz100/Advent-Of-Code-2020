from typing import List
from solutions.common.file_reader import FileReader


def find_triplet_that_sums_to_given_number(numbers: List[int], desired_result: int):
    for number in numbers:
        result_for_given_first_value = find_pair_that_sums_to_given_number(numbers, desired_result - number)
        if result_for_given_first_value is not None:
            return number, result_for_given_first_value[0], result_for_given_first_value[1]


def find_pair_that_sums_to_given_number(numbers: List[int], desired_result: int):
    processed_numbers = set()
    for number in numbers:
        if desired_result - number in processed_numbers:
            return number, desired_result - number
        processed_numbers.add(number)


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_line_list("input.txt")]
    result = find_pair_that_sums_to_given_number(puzzle_input, 2020)
    if result is not None:
        print("Part 1: result is ({}, {}) and their product: {}".format(result[0], result[1], result[0] * result[1]))

    result = find_triplet_that_sums_to_given_number(puzzle_input, 2020)
    if result is not None:
        print("Part 2: result is ({}, {}, {}) and their product: {}".format(
            result[0], result[1], result[2], result[0] * result[1] * result[2]))
