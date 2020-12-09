from solutions.common.algorithms import find_pair_that_sums_to_given_number
from solutions.common.file_reader import FileReader


def is_sum_of_any_from_list(value, numbers):
    return find_pair_that_sums_to_given_number(numbers, value) is not None


def find_first_invalid_number(numbers, preamble_length):
    for index, number in enumerate(numbers[preamble_length:]):
        if not is_sum_of_any_from_list(number, numbers[index:(index + preamble_length)]):
            return number


def find_subarray_with_given_sum(numbers, desired_sum):
    for window_size in range(2, len(numbers) + 1):
        for starting_index in range(0, len(numbers) - window_size + 1):
            if sum(numbers[starting_index:starting_index + window_size]) == desired_sum:
                return numbers[starting_index:starting_index + window_size]


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_line_list("input.txt")]
    first_invalid_number = find_first_invalid_number(puzzle_input, 25)
    print("[Part 1] First invalid number: {}".format(first_invalid_number))

    subarray = find_subarray_with_given_sum(puzzle_input, first_invalid_number)
    print("[Part 2] Encryption weakness: {}".format(min(subarray) + max(subarray)))
