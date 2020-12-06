from solutions.common.file_reader import FileReader


def merge_answers(answers):
    return ''.join(answers), len(answers)


def count_answers_given_by_each_member(group_info):
    unique_answers = set(group_info[0])
    return len(list(filter(lambda x: group_info[0].count(x) == group_info[1], unique_answers)))


if __name__ == '__main__':
    puzzle_input = FileReader.to_string("input.txt")
    group_answers = [merge_answers(group_str.splitlines()) for group_str in puzzle_input.split("\n\n")]
    answers_given_by_each_member = [count_answers_given_by_each_member(x) for x in group_answers]
    print("Total sum: {}".format(sum(answers_given_by_each_member)))
