from solutions.common.file_reader import FileReader
from solutions.day17.pocket_dimension import apply_automaton_rules, is_active, \
    empty_n_dimensional_grid, initialize_n_dimensional_grid_with_2d_pattern, \
    count_active_cubes_in_n_dimensional_grid, evaluate_n_cycles


def advance_to_next_cycle(grid, width, height, depth):
    new_grid = empty_n_dimensional_grid([width, height, depth])
    for z in range(1, depth - 1):
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                active_neighbours = count_active_neighbours(grid, x, y, z)
                new_grid[z][y][x] = apply_automaton_rules(grid[z][y][x], active_neighbours)
    return new_grid


def count_active_neighbours(grid, x, y, z):
    active = 0
    for z_dir in [-1, 0, 1]:
        for y_dir in [-1, 0, 1]:
            for x_dir in [-1, 0, 1]:
                if z_dir == 0 and y_dir == 0 and x_dir == 0:
                    continue
                active += is_active(grid[z + z_dir][y + y_dir][x + x_dir])
    return active


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    number_of_cycles = 6
    n_dim = 3

    grid_dimensions = [
        len(puzzle_input[0]) + 2 * (number_of_cycles + 1),  # width
        len(puzzle_input) + 2 * (number_of_cycles + 1),  # height
        1 + 2 * (number_of_cycles + 1)  # depth
    ]
    pocket_dimension_grid = empty_n_dimensional_grid(grid_dimensions)
    initialize_n_dimensional_grid_with_2d_pattern(puzzle_input, number_of_cycles, pocket_dimension_grid, n_dim)
    pocket_dimension_grid = evaluate_n_cycles(pocket_dimension_grid, grid_dimensions, number_of_cycles,
                                              advance_to_next_cycle)
    print("Number of active cubes: {}".format(count_active_cubes_in_n_dimensional_grid(pocket_dimension_grid, n_dim)))
