import operator
from solutions.day12.point_on_map import PointOnMap


class Ship(PointOnMap):

    directions_after_90_degrees_left_turn = dict({
        "E": "N", "N": "W", "W": "S", "S": "E"
    })

    def __init__(self):
        super().__init__(0, 0)
        self.direction = "E"

    def move_forward(self, distance):
        self.position = tuple(map(operator.add,
                                  self.position,
                                  tuple([distance * x for x in self.movement_modifiers_by_directions[self.direction]])))

    def move_to_waypoint(self, waypoint, number_of_times):
        for i in range(number_of_times):
            self.position = tuple(map(operator.add, self.position, waypoint.position))

    def turn(self, direction, degrees):
        number_of_rotations = int(degrees / 90) % 4
        number_of_90_degree_left_turns = number_of_rotations if direction == "L" else 4 - number_of_rotations
        for turn in range(number_of_90_degree_left_turns):
            self.direction = self.directions_after_90_degrees_left_turn[self.direction]
