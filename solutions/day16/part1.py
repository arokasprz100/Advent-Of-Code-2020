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


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    empty_line_indexes = [i for i, x in enumerate(puzzle_input) if x == '']
    ticket_fields_rules = puzzle_input[:empty_line_indexes[0]]
    nearby_tickets = [tickets.split(",") for tickets in puzzle_input[(empty_line_indexes[1] + 2):]]
    ticket_fields_rules = parse_ticket_fields_rules(ticket_fields_rules)
    all_possible_ranges = [value_range for value_ranges in ticket_fields_rules.values() for value_range in value_ranges]
    all_values_in_nearby_tickets = [int(value) for ticket_values in nearby_tickets for value in ticket_values]
    print(all_values_in_nearby_tickets)

    invalid_values = [value for value in all_values_in_nearby_tickets if not any([value in value_range for value_range in all_possible_ranges])]
    print(sum(invalid_values))
