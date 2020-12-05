from solutions.common.file_reader import FileReader


def binary_space_partitioning(space, instruction):
    if len(space) == 1:
        return space[0]
    elif instruction[0] == 'F' or instruction[0] == 'L':
        return binary_space_partitioning(space[:int(len(space)/2)], instruction[1:])
    else:
        return binary_space_partitioning(space[int(len(space)/2):], instruction[1:])


def find_row_and_column(instructions):
    row = binary_space_partitioning(range(0, 128), instructions[:7])
    column = binary_space_partitioning(range(0, 8), instructions[7:])
    return row, column


def seat_id(row, column):
    return row * 8 + column


def find_first_pair_with_one_number_between(numbers):
    sorted_numbers = sorted(numbers)
    for i, number in enumerate(sorted_numbers[:-1]):
        if sorted_numbers[i + 1] == sorted_numbers[i] + 2:
            return number, number + 2


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    seats = [find_row_and_column(boarding_pass) for boarding_pass in puzzle_input]
    seat_IDs = [seat_id(*seat) for seat in seats]
    print("Highest seat ID: {}".format(max(seat_IDs)))

    my_seat_ID = find_first_pair_with_one_number_between(seat_IDs)[0] + 1
    print("My seat ID: {}".format(my_seat_ID))
