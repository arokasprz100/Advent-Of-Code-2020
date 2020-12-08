from solutions.common.file_reader import FileReader
from solutions.day08.instruction_factory import InstructionFactory
from solutions.day08.registers import Registers


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    instruction_factory = InstructionFactory()
    instructions = [instruction_factory.get_instruction(line) for line in puzzle_input]
    while True:
        current_instruction = instructions[Registers.program_counter]
        if current_instruction.execution_counter == 1:
            break
        current_instruction.execute()

    print("Accumulator value: {}".format(Registers.accumulator))
