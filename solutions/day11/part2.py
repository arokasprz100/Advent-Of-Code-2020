import operator

from solutions.common.file_reader import FileReader
from solutions.day11.ferry_seats_cellular_automaton import FerrySeatsCellularAutomaton


def check_occupied_seat_existence_in_given_direction(cellular_automaton, x, y, direction):
    currently_checked_position = tuple(map(operator.add, (x, y), direction))
    while cellular_automaton.is_inside_board(currently_checked_position):
        if cellular_automaton.layout[currently_checked_position[1]][currently_checked_position[0]] == 'L':
            return False
        elif cellular_automaton.evaluate_position(currently_checked_position[0], currently_checked_position[1]):
            return True
        currently_checked_position = tuple(map(operator.add, currently_checked_position, direction))
    return False


def evaluate_part_two_neighbourhood(cellular_automaton, x, y):
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    occupied_seats_in_each_direction = list(map(
        lambda direction: check_occupied_seat_existence_in_given_direction(cellular_automaton, x, y, direction),
        directions))
    return sum(occupied_seats_in_each_direction)


def apply_part_two_rules(neighbourhood_value, current_state):
    if current_state == 'L' and neighbourhood_value == 0:
        return '#'
    elif current_state == '#' and neighbourhood_value >= 5:
        return 'L'
    return current_state


if __name__ == '__main__':
    puzzle_input = [list(x) for x in FileReader.to_line_list("input.txt")]
    ca = FerrySeatsCellularAutomaton(puzzle_input, evaluate_part_two_neighbourhood, apply_part_two_rules)
    ca.evaluate_until_no_change()
    print("Number of occupied seats: {}".format(ca.count_occupied_seats()))
