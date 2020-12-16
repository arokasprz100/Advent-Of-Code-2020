from solutions.common.file_reader import FileReader


def parse_ticket_fields_rules(rules):
    parsed_rules = {}
    for rule in rules:
        parts = rule.split(':')
        parsed_rules[parts[0]] = [parse_ticket_field_rule_range(x.strip()) for x in parts[1].split("or")]
    return parsed_rules


def parse_ticket_field_rule_range(range_str):
    parts = range_str.split("-")
    return range(int(parts[0]), int(parts[1]) + 1)


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


def parse_ticket_values(ticket_values_str):
    values = ticket_values_str.split(",")
    return [int(value) for value in values]


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    empty_line_indexes = [i for i, x in enumerate(puzzle_input) if x == '']
    ticket_fields_rules = parse_ticket_fields_rules(puzzle_input[:empty_line_indexes[0]])
    nearby_tickets = [parse_ticket_values(ticket) for ticket in puzzle_input[(empty_line_indexes[1] + 2):]]

    all_possible_ranges = [value_range for value_ranges in ticket_fields_rules.values() for value_range in value_ranges]
    invalid_tickets, invalid_values = find_invalid_tickets_and_values(nearby_tickets, all_possible_ranges)
    print("[PART 1] Ticket scanning error rate: {}".format(sum(invalid_values)))

    valid_nearby_tickets = [ticket for index, ticket in enumerate(nearby_tickets) if index not in invalid_tickets]
