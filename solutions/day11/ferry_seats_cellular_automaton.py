import copy


class FerrySeatsCellularAutomaton:

    def __init__(self, initial_layout, neighbours_evaluator, rules):
        self.neighbours_evaluator = neighbours_evaluator
        self.rules = rules
        self.layout = initial_layout
        self.layout_height = len(initial_layout)
        self.layout_width = len(initial_layout[0])

    def is_inside_board(self, position):
        return 0 <= position[0] < self.layout_width and 0 <= position[1] < self.layout_height

    def evaluate_position(self, x, y):
        if self.is_inside_board((x, y)):
            return int(self.layout[y][x] == '#')
        return 0

    def evaluate_one_step(self):
        new_layout = copy.deepcopy(self.layout)
        for y in range(self.layout_height):
            for x in range(self.layout_width):
                neighbours_value = self.neighbours_evaluator(self, x, y)
                new_layout[y][x] = self.rules(neighbours_value, self.layout[y][x])
        self.layout = new_layout

    def do_layouts_differ(self, layoutA, layoutB):
        for y in range(self.layout_height):
            for x in range(self.layout_width):
                if layoutA[y][x] != layoutB[y][x]:
                    return True
        return False

    def evaluate_until_no_change(self):
        while True:
            current_layout = self.layout
            self.evaluate_one_step()
            if not self.do_layouts_differ(current_layout, self.layout):
                break

    def count_occupied_seats(self):
        return sum(sum(1 if cell == '#' else 0 for cell in row) for row in self.layout)
