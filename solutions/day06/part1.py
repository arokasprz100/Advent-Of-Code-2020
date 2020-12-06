from solutions.common.file_reader import FileReader

if __name__ == '__main__':
    puzzle_input = FileReader.to_string("input.txt")
    answers_in_groups = [set(''.join(group_str.splitlines())) for group_str in puzzle_input.split("\n\n")]
    numbers_of_answers_in_groups = [len(group) for group in answers_in_groups]
    print("Total sum: {}".format(sum(numbers_of_answers_in_groups)))
