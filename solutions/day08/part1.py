from solutions.common.file_reader import FileReader
from solutions.day08.instruction_factory import InstructionFactory
from solutions.day08.program_runner import ProgramRunner


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    instruction_factory = InstructionFactory()
    instructions = [instruction_factory.get_instruction(line) for line in puzzle_input]
    program_runner = ProgramRunner(instructions)
    program_runner.until_exit_condition_met()
    print("Accumulator value: {}".format(program_runner.registers.accumulator))
