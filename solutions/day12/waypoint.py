from solutions.day12.point_on_map import PointOnMap


class Waypoint(PointOnMap):

    def __init__(self):
        super().__init__(10, 1)

    def rotate(self, direction, degrees):
        number_of_rotations = int(degrees / 90) % 4
        number_of_90_degree_left_turns = number_of_rotations if direction == "L" else 4 - number_of_rotations
        for turn in range(number_of_90_degree_left_turns):
            self.position = -self.position[1], self.position[0]
