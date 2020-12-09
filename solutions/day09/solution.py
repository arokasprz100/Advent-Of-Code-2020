from solutions.common.file_reader import FileReader


def is_sum_of_any_from_list(value, numbers):
    processed_numbers = set()
    for number in numbers:
        if value - number in processed_numbers:
            return True
        processed_numbers.add(number)
    return False


def find_first_invalid_number(numbers, preamble_length):
    for index, number in enumerate(numbers[preamble_length:]):
        if not is_sum_of_any_from_list(number, numbers[index:(index + preamble_length)]):
            return number


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_line_list("input.txt")]
    first_invalid_number = find_first_invalid_number(puzzle_input, 25)
    print("[Part 1] First invalid number: {}".format(first_invalid_number))
