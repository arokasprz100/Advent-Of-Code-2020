def parse_ticket_fields_rules(rules):
    parsed_rules = {}
    for rule in rules:
        parts = rule.split(':')
        parsed_rules[parts[0]] = [parse_ticket_field_rule_range(x.strip()) for x in parts[1].split("or")]
    return parsed_rules


def parse_ticket_field_rule_range(range_str):
    parts = range_str.split("-")
    return range(int(parts[0]), int(parts[1]) + 1)


def parse_ticket_values(ticket_values_str):
    values = ticket_values_str.split(",")
    return [int(value) for value in values]
