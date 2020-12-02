from solutions.common.file_reader import FileReader
from solutions.day02.puzzle_input_parser import parse_puzzle_input


def validate_password(first_position, second_position, letter, password):
    return (password[first_position - 1] == letter) ^ (password[second_position - 1] == letter)


if __name__ == '__main__':
    puzzle_input = parse_puzzle_input(FileReader.to_line_list("input.txt"))
    number_of_valid_passwords = len([entry for entry in puzzle_input if validate_password(*entry)])
    print(number_of_valid_passwords)
