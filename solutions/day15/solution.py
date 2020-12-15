from solutions.common.file_reader import FileReader


def get_nth_spoken_number(starting_numbers, n):
    spoken_numbers = {number: turn + 1 for turn, number in enumerate(starting_numbers[:-1])}
    last_spoken_number = starting_numbers[-1]
    for current_turn in range(len(puzzle_input), n):
        next_number = 0 if last_spoken_number not in spoken_numbers \
            else current_turn - spoken_numbers[last_spoken_number]
        spoken_numbers[last_spoken_number] = current_turn
        last_spoken_number = next_number
    return last_spoken_number


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_string("input.txt").split(",")]
    part1_answer = get_nth_spoken_number(puzzle_input, 2020)
    print("[PART 1] 2020th number spoken: {}".format(part1_answer))
    part2_answer = get_nth_spoken_number(puzzle_input, 30000000)
    print("[PART 2] 30000000th number spoken: {}".format(part2_answer))
