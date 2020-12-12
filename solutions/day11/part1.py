from solutions.common.file_reader import FileReader
from solutions.day11.ferry_seats_cellular_automaton import FerrySeatsCellularAutomaton


def evaluate_moore_neighbourhood(cellular_automaton, x, y):
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    occupied_seats_in_each_direction = list(map(
        lambda direction: cellular_automaton.evaluate_position(x + direction[0], y + direction[1]), directions))
    return sum(occupied_seats_in_each_direction)


def apply_part_one_rules(neighbourhood_value, current_state):
    if current_state == 'L' and neighbourhood_value == 0:
        return '#'
    elif current_state == '#' and neighbourhood_value >= 4:
        return 'L'
    return current_state


if __name__ == '__main__':
    puzzle_input = [list(x) for x in FileReader.to_line_list("input.txt")]
    ca = FerrySeatsCellularAutomaton(puzzle_input, evaluate_moore_neighbourhood, apply_part_one_rules)
    ca.evaluate_until_no_change()
    print("Number of occupied seats: {}".format(ca.count_occupied_seats()))
