import copy
from solutions.common.file_reader import FileReader
from solutions.day08.instruction_factory import InstructionFactory
from solutions.day08.instructions import JumpInstruction, NOPInstruction
from solutions.day08.program_runner import ProgramRunner, ExitCondition


def swap_instruction_and_execute(instructions, instruction_number):
    instructions_copy = copy.deepcopy(instructions)
    checked_instruction = instructions_copy[instruction_number]
    if isinstance(checked_instruction, JumpInstruction):
        instructions_copy[instruction_number] = NOPInstruction(checked_instruction.argument)
    elif isinstance(checked_instruction, NOPInstruction):
        instructions_copy[instruction_number] = JumpInstruction(checked_instruction.argument)
    else:
        return None
    program_runner = ProgramRunner(instructions_copy)
    exit_condition = program_runner.until_exit_condition_met()
    return program_runner.registers.accumulator if exit_condition == ExitCondition.TERMINATION else None


if __name__ == '__main__':
    puzzle_input = FileReader.to_line_list("input.txt")
    instruction_factory = InstructionFactory()
    original_instructions = [instruction_factory.get_instruction(line) for line in puzzle_input]
    for number in range(len(original_instructions)):
        result = swap_instruction_and_execute(original_instructions, number)
        if result:
            print("Value in accumulator: {}".format(result))
            break
