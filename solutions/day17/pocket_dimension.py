def empty_n_dimensional_grid(dimensions):
    if len(dimensions) == 1:
        return ['.' for _ in range(dimensions[0])]
    return [empty_n_dimensional_grid(dimensions[:-1]) for _ in range(dimensions[-1])]


def initialize_n_dimensional_grid_with_2d_pattern(pattern, cycles, grid, n):
    if n > 2:
        initialize_n_dimensional_grid_with_2d_pattern(pattern, cycles, grid[cycles + 1], n - 1)
    else:
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                grid[cycles + 1 + y][cycles + 1 + x] = pattern[y][x]


def apply_automaton_rules(current_cube, number_of_active_neighbours):
    if current_cube == '#' and (number_of_active_neighbours == 2 or number_of_active_neighbours == 3):
        return '#'
    elif current_cube == '#':
        return '.'
    elif current_cube == '.' and number_of_active_neighbours == 3:
        return '#'
    else:
        return '.'


def is_active(cube):
    return cube == '#'


def count_active_cubes_in_n_dimensional_grid(grid, n):
    return sum([is_active(cube) for cube in grid]) if n == 1 \
        else sum([count_active_cubes_in_n_dimensional_grid(sub_grid, n - 1) for sub_grid in grid])


def evaluate_n_cycles(grid, grid_dimensions, n, cycle_advancement_strategy):
    for _ in range(n):
        grid = cycle_advancement_strategy(grid, *grid_dimensions)
    return grid
