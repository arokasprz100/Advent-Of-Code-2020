import itertools

from solutions.common.file_reader import FileReader
from solutions.day14.instruction_runner import InstructionRunner


def apply_mask_single_bit(mask_bit, addr_bit):
    if mask_bit == '0':
        return addr_bit
    return mask_bit


def apply_mask_on_address(bitmask, addr):
    addr_binary = "{0:b}".format(addr).zfill(36)
    result = ''.join([apply_mask_single_bit(x[0], x[1]) for x in zip(bitmask, addr_binary)])
    return result


def generate_all_addresses(addr):
    number_of_floating = addr.count('X')
    all_possibilities = list(itertools.product(['0', '1'], repeat=number_of_floating))
    addresses = [replace_floating_values(addr, possible_value_arrangement)
                 for possible_value_arrangement in all_possibilities]
    return [int(x, 2) for x in addresses]


def replace_floating_values(addr, possible_value_arrangement):
    for bit in possible_value_arrangement:
        addr = addr.replace("X", bit, 1)
    return addr


def generate_addresses_and_assign_value(memory, mask, address, value):
    address_with_mask = apply_mask_on_address(mask, address)
    generated_addresses = generate_all_addresses(address_with_mask)
    for generated_address in generated_addresses:
        memory[generated_address] = value


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    runner = InstructionRunner(generate_addresses_and_assign_value)
    runner.run(puzzle_input)
    print("Sum of all values in the memory: {}".format(sum(runner.memory.values())))
