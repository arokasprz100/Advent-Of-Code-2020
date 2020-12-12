import operator


class PointOnMap:

    movement_modifiers_by_directions = dict({
        "N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)
    })

    def __init__(self, start_x, start_y):
        self.position = (start_x, start_y)

    def move_in_cardinal_direction(self, direction, distance):
        self.position = tuple(map(operator.add,
                                  self.position,
                                  tuple([distance * x for x in self.movement_modifiers_by_directions[direction]])))
