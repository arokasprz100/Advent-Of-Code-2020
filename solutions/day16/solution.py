import math

from solutions.common.file_reader import FileReader
from solutions.day16.parsing import parse_ticket_fields_rules, parse_ticket_values


def find_invalid_tickets_and_values(tickets, possible_ranges):
    all_invalid_values = []
    invalid_ticket_indexes = []
    for index, ticket in enumerate(tickets):
        ticket_invalid_values = [value for value in ticket if not any([value in value_range
                                                                       for value_range in possible_ranges])]
        if ticket_invalid_values:
            all_invalid_values.extend(ticket_invalid_values)
            invalid_ticket_indexes.append(index)
    return invalid_ticket_indexes, all_invalid_values


def get_fields_suitable_for_position(position, rules, tickets, possible_fields):
    suitable_fields = []
    for field_name in possible_fields:
        if check_if_for_all_tickets_value_at_given_position_follow_field_rules(position, rules, tickets, field_name):
            suitable_fields.append(field_name)
    return suitable_fields


def check_if_for_all_tickets_value_at_given_position_follow_field_rules(position, rules, tickets, field_name):
    for ticket in tickets:
        valid_ranges = [valid_range for valid_range in rules[field_name] if ticket[position] in valid_range]
        if not valid_ranges:
            return False
    return True


def remove_fields_that_are_required_on_some_position_from_other_positions(fields_for_each_position):
    required_at_some_position = [x[0] for x in filter(lambda x: len(x) == 1, fields_for_each_position)]
    for position in range(len(fields_for_each_position)):
        if len(fields_for_each_position[position]) > 1:
            fields_for_each_position[position] = [x for x in fields_for_each_position[position]
                                                  if x not in required_at_some_position]


def all_positions_have_exactly_one_field(fields_for_each_position):
    return all([len(fields) == 1 for fields in fields_for_each_position])


def determine_right_fields_order(rules, tickets, field_names):
    fields_suitable_for_each_position = [get_fields_suitable_for_position(position, rules, tickets, field_names)
                                         for position in range(len(field_names))]
    while not all_positions_have_exactly_one_field(fields_suitable_for_each_position):
        remove_fields_that_are_required_on_some_position_from_other_positions(fields_suitable_for_each_position)
    return [x[0] for x in fields_suitable_for_each_position]


def get_positions_of_fields_that_start_with_departure(fields_in_order):
    return [index for index, field_name in enumerate(fields_in_order) if field_name.startswith("departure")]


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")

    empty_line_indexes = [i for i, x in enumerate(puzzle_input) if x == '']
    ticket_fields_rules = parse_ticket_fields_rules(puzzle_input[:empty_line_indexes[0]])
    my_ticket = parse_ticket_values(puzzle_input[empty_line_indexes[1] - 1])
    nearby_tickets = [parse_ticket_values(ticket) for ticket in puzzle_input[(empty_line_indexes[1] + 2):]]

    all_possible_ranges = [value_range for value_ranges in ticket_fields_rules.values() for value_range in value_ranges]
    invalid_tickets, invalid_values = find_invalid_tickets_and_values(nearby_tickets, all_possible_ranges)
    print("[PART 1] Ticket scanning error rate: {}".format(sum(invalid_values)))

    valid_nearby_tickets = [ticket for index, ticket in enumerate(nearby_tickets) if index not in invalid_tickets]
    fields_order = determine_right_fields_order(ticket_fields_rules, valid_nearby_tickets, ticket_fields_rules.keys())
    positions_of_departure_fields = get_positions_of_fields_that_start_with_departure(fields_order)
    desired_values_product = math.prod([my_ticket[index] for index in positions_of_departure_fields])
    print("[PART 2] Product of fields that start with 'departure' on my ticket: {}".format(desired_values_product))
