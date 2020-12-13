from functools import reduce
from solutions.common.file_reader import FileReader


def compute_the_earliest_timestamp_that_fulfills_the_requirements(buses_with_offsets):
    """
    This solution is heavily based on my observation: all bus IDs (in this exercise bus ID
    describes, how often the bus leaves for the airport - it's an interval) are prime numbers
    (and this is true for both my puzzle input and the example shown in exercise description).
    Because of that, any two bus IDs are pairwise co-prime (their GCD is equal to one). \n
    Thanks to this observation, this solution can use the Chinese Remainder Theorem. For more
    info, see: https://en.wikipedia.org/wiki/Chinese_remainder_theorem (to understand this solution,
    read the 'Existence (direct construction)' subsection. \n
    In this case, we denote the bus_id as n_i, and the desired interval as x. We can write the
    following sequence of congruence equations: \n
    x = remainder_1 (mod n_1) \n
    ... \n
    x = remainder_k (mod n_k) \n
    Where each reminder_i = bus_id - bus_offset (for example, if the offset is equal to 1, and
    the bus_id is equal to 13, the remainder will be equal to 12, because if for example the
    x is equal to 1068781, to can be written as: 1068781 = 12 (mod 13)). Then we find the x (which
    is the timestamp we are looking for). \n
    To read more in polish: http://ww2.ii.uj.edu.pl/~wilczak/ilo/pdf/twierdzenie_chinskie.pdf

    :param buses_with_offsets: Formatted puzzle input - list of tuples (bus_id, bus_offset)
    :return: Resulting timestamp that is the exercise solution.
    """
    remainders = list(map(lambda bus_with_offset: bus_with_offset[0] - bus_with_offset[1], buses_with_offsets))
    n_i = list(map(lambda bus_with_offset: bus_with_offset[0], buses_with_offsets))
    N = reduce(lambda x, y: x * y, n_i)  # n_1 * n_2 ... * n_k
    N_i = list(map(lambda n: N // n, n_i))  # N // n_i for each i
    M_i = list(map(lambda i: compute_bezout_coefficients(N_i[i], n_i[i])[0], range(len(N_i))))  # Bezout coefficient
    return sum(map(lambda x: x[0] * x[1] * x[2], list(zip(remainders, N_i, M_i)))) % N


def extended_gcd(a, b):
    """
    Based on https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    :param a: Input integer.
    :param b: Input integer.
    :return: Tuple with following elements: (greatest common divisor, Bezout coefficient 1, Bezout coefficient 2)
    """
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def compute_bezout_coefficients(a, b):
    """
    Computes x and y coefficients according to Bezout's identity: ax + by = d (in out case, d = 1, because
    in our case a and b are co-prime).
    :param a: Input integer.
    :param b: Input integer.
    :return: Two integers x and y - the Bezout coefficients for (a, b).
    """
    _, x, y = extended_gcd(a, b)
    return x, y


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    buses_with_indexes = [(int(x[1]), x[0]) for x in enumerate(puzzle_input[1].split(',')) if x[1] != 'x']
    earliest_timestamp = compute_the_earliest_timestamp_that_fulfills_the_requirements(buses_with_indexes)
    print("Earliest timestamp: {}".format(earliest_timestamp))
