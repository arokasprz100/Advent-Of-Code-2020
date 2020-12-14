from solutions.common.file_reader import FileReader
from solutions.day07.bag_rules_parsing import parse_bag_rule


def search_for_shiny_gold_bags(color_of_bag_to_search, bags_collection):
    nested_bags = bags_collection[color_of_bag_to_search]
    if not nested_bags:
        return False
    shiny_gold_in_nested = [True if nested_bag_color == "shiny gold"
                            else search_for_shiny_gold_bags(nested_bag_color, bags_collection)
                            for nested_bag_color, nested_bag_count in nested_bags]
    return any(shiny_gold_in_nested)


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    bag_details = [parse_bag_rule(bag_rule) for bag_rule in puzzle_input]
    bags = {bag[0]: bag[1] for bag in bag_details}
    bags_contain_shiny_gold_one = {bag_color: search_for_shiny_gold_bags(bag_color, bags) for bag_color in bags}
    number_of_containing_shiny_gold_one = len(list(filter(lambda x: x[1] is True, bags_contain_shiny_gold_one.items())))
    print("There are {} bags that contain shiny gold bag.".format(number_of_containing_shiny_gold_one))
