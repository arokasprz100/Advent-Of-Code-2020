from solutions.common.file_reader import FileReader
from solutions.day12.ship import Ship
from solutions.day12.waypoint import Waypoint


def execute_single_instruction(navigated_ship, ship_waypoint, instruction):
    action = instruction[0]
    value = int(instruction[1:])
    if action in ["N", "W", "E", "S"]:
        ship_waypoint.move_in_cardinal_direction(action, value)
    elif action in ["L", "R"]:
        ship_waypoint.rotate(action, value)
    else:
        navigated_ship.move_to_waypoint(ship_waypoint, value)


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    ship = Ship()
    waypoint = Waypoint()
    for instr in puzzle_input:
        execute_single_instruction(ship, waypoint, instr)
    manhattan_distance = abs(ship.position[0]) + abs(ship.position[1])
    print("Manhattan distance from starting position: {}".format(manhattan_distance))
