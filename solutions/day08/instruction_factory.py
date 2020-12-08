from solutions.day08.instructions import AccInstruction, NOPInstruction, JumpInstruction


class InstructionFactory:

    def __init__(self):
        self.instructions_by_mnemonics = dict({
            "acc": lambda argument: AccInstruction(argument),
            "nop": lambda argument: NOPInstruction(argument),
            "jmp": lambda argument: JumpInstruction(argument)})

    def get_instruction(self, text_representation):
        parts = text_representation.split(" ")
        mnemonic = parts[0]
        argument = int(parts[1])
        return self.instructions_by_mnemonics[mnemonic](argument)
