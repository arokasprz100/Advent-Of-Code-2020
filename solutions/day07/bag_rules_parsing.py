import re


def parse_bag_rule(rule):
    rule_parts_search = re.search("(.*) bags contain (.*).", rule)
    bag_color = rule_parts_search.group(1)
    if rule_parts_search.group(2) == "no other bags":
        return bag_color, []
    contained_bags = [parse_contained_bag(bag) for bag in rule_parts_search.group(2).split(", ")]
    return bag_color, contained_bags


def parse_contained_bag(bag):
    parts = bag.split(" ")
    return parts[1] + " " + parts[2], int(parts[0])