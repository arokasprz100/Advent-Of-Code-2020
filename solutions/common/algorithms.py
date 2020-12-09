def find_pair_that_sums_to_given_number(numbers, desired_result):
    processed_numbers = set()
    for number in numbers:
        if desired_result - number in processed_numbers:
            return number, desired_result - number
        processed_numbers.add(number)
