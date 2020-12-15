from solutions.day14.instruction_parsing import parse_bitmask_instruction, parse_memory_assignment_instruction


class InstructionRunner:

    def __init__(self, memory_assignment_strategy):
        self.memory_assignment_strategy = memory_assignment_strategy
        self.memory = dict({})
        self.mask = 'X' * 36

    def replace_mask(self, instruction):
        self.mask = parse_bitmask_instruction(instruction)

    def assign_value_to_memory(self, instruction):
        address, value = parse_memory_assignment_instruction(instruction)
        self.memory_assignment_strategy(self.memory, self.mask, address, value)

    def run(self, instructions):
        for instruction in instructions:
            if instruction.startswith("mask = "):
                self.replace_mask(instruction)
            elif instruction.startswith("mem"):
                self.assign_value_to_memory(instruction)
