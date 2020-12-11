from solutions.common.file_reader import FileReader
from solutions.day10.distinct_adapters_arrangements import count_number_of_distinct_adapters_arrangements


def build_chain_using_all_adapters(available_adapters):
    return sorted(available_adapters)


def count_given_differences(chain, value):
    return len(list(filter(lambda x: x[0] - x[1] == value, zip(chain[1:], chain[:-1]))))


if __name__ == '__main__':
    puzzle_input = [int(x) for x in FileReader.to_line_list("input.txt")]
    built_in_adapter = max(puzzle_input) + 3
    valid_chain = [0] + build_chain_using_all_adapters(puzzle_input) + [built_in_adapter]
    number_of_one_jolt_differences = count_given_differences(valid_chain, 1)
    number_of_three_jolt_differences = count_given_differences(valid_chain, 3)
    print("[PART 1] Number of one jolt differences: {}".format(number_of_one_jolt_differences))
    print("[PART 1] Number of three jolt differences: {}".format(number_of_three_jolt_differences))
    print("[PART 1] Product: {}".format(number_of_one_jolt_differences * number_of_three_jolt_differences))
    print("[PART 2] Number of distinct adapters arrangements: {}".format(
        count_number_of_distinct_adapters_arrangements(valid_chain)))
