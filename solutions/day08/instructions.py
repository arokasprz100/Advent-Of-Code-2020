from abc import ABC, abstractmethod
from solutions.day08.registers import Registers


class SingleArgInstruction(ABC):

    def __init__(self, argument):
        self.argument = argument
        self.execution_counter = 0

    @abstractmethod
    def execute(self):
        pass

    def increase_execution_counter(self):
        self.execution_counter += 1


class NOPInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self):
        Registers.program_counter += 1
        self.increase_execution_counter()


class JumpInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self):
        Registers.program_counter += self.argument
        self.increase_execution_counter()


class AccInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self):
        Registers.accumulator += self.argument
        Registers.program_counter += 1
        self.increase_execution_counter()