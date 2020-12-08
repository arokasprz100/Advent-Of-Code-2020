from abc import ABC, abstractmethod


class SingleArgInstruction(ABC):

    def __init__(self, argument):
        self.argument = argument
        self.execution_counter = 0

    @abstractmethod
    def execute(self, registers):
        pass

    def increase_execution_counter(self):
        self.execution_counter += 1


class NOPInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self, registers):
        registers.program_counter += 1
        self.increase_execution_counter()


class JumpInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self, registers):
        registers.program_counter += self.argument
        self.increase_execution_counter()


class AccInstruction(SingleArgInstruction):

    def __init__(self, argument):
        super().__init__(argument)

    def execute(self, registers):
        registers.accumulator += self.argument
        registers.program_counter += 1
        self.increase_execution_counter()
