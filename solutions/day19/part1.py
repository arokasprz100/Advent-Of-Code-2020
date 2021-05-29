from solutions.common.file_reader import FileReader
import re


def parse_rule(rule):
    parts = rule.split(':')
    rule_number = int(parts[0])
    rule_details = [x.strip().split(' ') for x in parts[1].split('|')]
    return rule_number, rule_details


def convert_rules_to_regex(rule_number, all_rules):
    rule = all_rules[rule_number]
    if isinstance(rule, list):
        results = []
        for alternative in rule:
            result = ''.join([convert_rules_to_regex(int(x), all_rules) if x.isdigit() else x.strip("\"") for x in alternative])
            results.append(result)
        return '({})'.format('|'.join(results))
    return rule


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    rules = {rule[0]: rule[1] for rule in [parse_rule(x) for x in puzzle_input[:puzzle_input.index('')]]}
    messages = puzzle_input[(puzzle_input.index('') + 1):]
    valid_message_regex = '^{}$'.format(convert_rules_to_regex(0, rules))
    valid_messages = [bool(re.match(valid_message_regex, message)) for message in messages]
    print(sum(valid_messages))






