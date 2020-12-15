from solutions.common.file_reader import FileReader
from solutions.day14.instruction_runner import InstructionRunner


def apply_mask_on_value(bitmask, val):
    val_binary = "{0:b}".format(val).zfill(36)
    result = ''.join([x[0] if x[0] != 'X' else x[1] for x in zip(bitmask, val_binary)])
    return int(result, 2)


def generate_value_and_assign_it_to_given_address(memory, mask, address, value):
    memory[address] = apply_mask_on_value(mask, value)


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    runner = InstructionRunner(generate_value_and_assign_it_to_given_address)
    runner.run(puzzle_input)
    print("Sum of all values in the memory: {}".format(sum(runner.memory.values())))
