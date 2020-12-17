from solutions.common.file_reader import FileReader


def empty_layer(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]


def empty_grid(width, height, depth):
    return [empty_layer(width, height) for _ in range(depth)]


def initialize_grid_with_starting_pattern(pattern, cycles, grid):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            grid[cycles + 1][cycles + 1 + y][cycles + 1 + x] = pattern[y][x]


def print_grid(grid):
    for layer in grid:
        for row in layer:
            print(''.join(row))
        print()


def advance_to_next_cycle(grid, width, height, depth):
    new_grid = empty_grid(width, height, depth)
    for z in range(1, depth - 1):
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                active_neighbours = count_active_neighbours(grid, x, y, z)
                new_grid[z][y][x] = apply_automaton_rules(grid[z][y][x], active_neighbours)
    return new_grid


def apply_automaton_rules(current_cube, number_of_active_neighbours):
    if current_cube == '#' and (number_of_active_neighbours == 2 or number_of_active_neighbours == 3):
        return '#'
    elif current_cube == '#':
        return '.'
    elif current_cube == '.' and number_of_active_neighbours == 3:
        return '#'
    else:
        return '.'


def count_active_neighbours(grid, x, y, z):
    active = 0
    for z_dir in [-1, 0, 1]:
        for y_dir in [-1, 0, 1]:
            for x_dir in [-1, 0, 1]:
                if z_dir == 0 and y_dir == 0 and x_dir == 0:
                    continue
                active += is_active(grid[z + z_dir][y + y_dir][x + x_dir])
    return active


def is_active(cube):
    return cube == '#'


def count_active_cubes(grid):
    active = 0
    for layer in grid:
        for row in layer:
            for cube in row:
                active += is_active(cube)
    return active


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    number_of_cycles = 6

    grid_max_width = len(puzzle_input[0]) + 2 * (number_of_cycles + 1)
    grid_max_height = len(puzzle_input) + 2 * (number_of_cycles + 1)
    grid_max_depth = 1 + 2 * (number_of_cycles + 1)

    pocket_dimension_grid = empty_grid(grid_max_width, grid_max_height, grid_max_depth)
    initialize_grid_with_starting_pattern(puzzle_input, number_of_cycles, pocket_dimension_grid)

    for _ in range(number_of_cycles):
        pocket_dimension_grid = advance_to_next_cycle(pocket_dimension_grid,
                                                      grid_max_width, grid_max_height, grid_max_depth)

    print_grid(pocket_dimension_grid)
    print(count_active_cubes(pocket_dimension_grid))
