from solutions.common.file_reader import FileReader
from solutions.day17.pocket_dimension import is_active, apply_automaton_rules, empty_n_dimensional_grid, \
    initialize_n_dimensional_grid_with_2d_pattern, evaluate_n_cycles, count_active_cubes_in_n_dimensional_grid


def count_active_neighbours(grid, x, y, z, w):
    active = 0
    for w_dir in [-1, 0, 1]:
        for z_dir in [-1, 0, 1]:
            for y_dir in [-1, 0, 1]:
                for x_dir in [-1, 0, 1]:
                    if z_dir == 0 and y_dir == 0 and x_dir == 0 and w_dir == 0:
                        continue
                    active += is_active(grid[w + w_dir][z + z_dir][y + y_dir][x + x_dir])
    return active


def advance_to_next_cycle(grid, width, height, depth, fourth_dimension):
    new_grid = empty_n_dimensional_grid([width, height, depth, fourth_dimension])
    for w in range(1, fourth_dimension - 1):
        for z in range(1, depth - 1):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    active_neighbours = count_active_neighbours(grid, x, y, z, w)
                    new_grid[w][z][y][x] = apply_automaton_rules(grid[w][z][y][x], active_neighbours)
    return new_grid


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    number_of_cycles = 6
    n_dim = 4

    grid_dimensions = [
        len(puzzle_input[0]) + 2 * (number_of_cycles + 1),
        len(puzzle_input) + 2 * (number_of_cycles + 1),
        1 + 2 * (number_of_cycles + 1),
        1 + 2 * (number_of_cycles + 1)
    ]

    pocket_dimension_grid = empty_n_dimensional_grid(grid_dimensions)
    initialize_n_dimensional_grid_with_2d_pattern(puzzle_input, number_of_cycles, pocket_dimension_grid, n_dim)
    pocket_dimension_grid = evaluate_n_cycles(pocket_dimension_grid, grid_dimensions, number_of_cycles,
                                              advance_to_next_cycle)
    print("Number of active cubes: {}".format(count_active_cubes_in_n_dimensional_grid(pocket_dimension_grid, n_dim)))
