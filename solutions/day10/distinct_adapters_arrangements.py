import math


def count_number_of_distinct_adapters_arrangements(chain_of_adapters):
    """
    This is my solution to part 2 of this exercise. Is is based on following algorithm:
        1) valid chain of adapters is sorted, and the difference between adjacent adapters is 1, 2 or 3
        2) problem can be divided into multiple smaller problems because if there is an element with a difference
        of 3 with any of its adjacent elements, this element can not be removed from the chain - for example if we
        have a sequence [1, 2, 3, 4, 7, 8, 9], we can not remove the 7 (it differs with 4 by 3), because removing
        it would render connecting 4 and 8 impossible
        3) the idea is to split the problem using those element with difference equal to 3 - each sub-chain will
        contain only elements with differences equal to 1 or 2, in this case: [1, 2, 3, 4] and [8, 9]
        4) for each of the sub-chains we calculate every possible (even invalid) sorted arrangement of adapters
        and then we remove invalid ones. We count the amount of valid possibilities for each sub-chain
        5) in the end, we multiply the results (excluding the zeros)
    Point 4 is most problematic, because the speed is highly dependent on the size of created sub-chains. I tried
    to come up with a formula to calculate number of valid arrangements for a given sub-chain, but I ended up just
    using this approach.
    :param chain_of_adapters: Valid chain that uses all adapters (found in part 1 of the exercise)
    :return: number of distinct adapters arrangement (can, but does not have to use them all)
    """
    sequences_with_difference_less_than_three = split_on_difference_three(chain_of_adapters)
    return math.prod(filter(lambda x: x > 0, [count_possibilities_to_rearrange_single_sub_sequence(sequence)
                                              for sequence in sequences_with_difference_less_than_three]))


def count_possibilities_to_rearrange_single_sub_sequence(subsequence):
    possible_adapter_arrangements = generate_all_arrangement_possibilities(subsequence, [])
    return count_valid_arrangements(subsequence[0], subsequence[-1], possible_adapter_arrangements)


def split_on_difference_three(chain):
    index_start = 0
    index_end = 1
    sub_chains = []
    while index_end < len(chain):
        while chain[index_end] - chain[index_end - 1] < 3:
            index_end = index_end + 1
        sub_chains.append(chain[index_start:index_end])
        index_start = index_end
        index_end = index_end + 1
    return sub_chains


def generate_all_arrangement_possibilities(available_adapters, current_chain):
    if not available_adapters:
        return [current_chain]
    to_check = available_adapters[0]
    with_placed = generate_all_arrangement_possibilities(available_adapters[1:], current_chain + [to_check])
    without_placed = generate_all_arrangement_possibilities(available_adapters[1:], current_chain)
    return [*with_placed, *without_placed]


def count_valid_arrangements(starting_value, ending_value, chains):
    return sum(map(lambda chain: validate_arrangement(starting_value, ending_value, chain), chains))


def validate_arrangement(start_value, end_value, chain):
    if len(chain) < 2 or chain[0] != start_value or chain[-1] != end_value:
        return False
    for index, entry in enumerate(chain[1:]):
        if chain[index + 1] - chain[index] > 3:
            return False
    return True
