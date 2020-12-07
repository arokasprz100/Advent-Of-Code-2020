from solutions.common.file_reader import FileReader
from solutions.day07.bag_rules_parsing import parse_bag_rule


def count_nested_bags(color_of_bag_to_search, bags_collection):
    nested_bags = bags_collection[color_of_bag_to_search]
    return 0 if not nested_bags else sum(
        [nested_bag_count + nested_bag_count * count_nested_bags(nested_bag_color, bags_collection)
         for nested_bag_color, nested_bag_count in nested_bags])


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    bag_details = [parse_bag_rule(bag_rule) for bag_rule in puzzle_input]
    bags = {bag[0]: bag[1] for bag in bag_details}
    print("Number of bags inside single shiny gold bag: {}".format(count_nested_bags("shiny gold", bags)))
