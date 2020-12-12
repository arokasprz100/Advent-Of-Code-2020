from solutions.common.file_reader import FileReader
from solutions.day12.ship import Ship


def execute_single_instruction(navigated, instruction):
    action = instruction[0]
    value = int(instruction[1:])
    if action in ["N", "W", "E", "S"]:
        navigated.move_in_cardinal_direction(action, value)
    elif action in ["L", "R"]:
        navigated.turn(action, value)
    else:
        navigated.move_forward(value)


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    ship = Ship()
    for instr in puzzle_input:
        execute_single_instruction(ship, instr)
    manhattan_distance = abs(ship.position[0]) + abs(ship.position[1])
    print("Manhattan distance from starting position: {}".format(manhattan_distance))
