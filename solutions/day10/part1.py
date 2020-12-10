from solutions.common.file_reader import FileReader


def build_chain_using_all_adapters(available_adapters):
    return sorted(available_adapters)


def count_given_differences(chain, value):
    return len(list(filter(lambda x: x[0] - x[1] == value, zip(chain[1:], chain[0:-1]))))


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_line_list("input.txt")]
    built_in_adapter = max(puzzle_input) + 3
    valid_chain = [0] + build_chain_using_all_adapters(puzzle_input) + [built_in_adapter]
    number_of_one_jolt_differences = count_given_differences(valid_chain, 1)
    number_of_three_jolt_differences = count_given_differences(valid_chain, 3)
    print(number_of_one_jolt_differences * number_of_three_jolt_differences)
