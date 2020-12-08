from solutions.day08.registers import Registers
from enum import Enum


class ExitCondition(Enum):
    INFINITE_LOOP = 1
    TERMINATION = 2


class ProgramRunner:

    def __init__(self, instructions):
        self.registers = Registers()
        self.instructions = instructions

    def until_exit_condition_met(self):
        while True:
            if self.registers.program_counter >= len(self.instructions):
                return ExitCondition.TERMINATION
            current_instruction = self.instructions[self.registers.program_counter]
            if current_instruction.execution_counter == 1:
                return ExitCondition.INFINITE_LOOP
            current_instruction.execute(self.registers)
