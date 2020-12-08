
class Registers:
    program_counter = 0
    accumulator = 0

    @classmethod
    def reset(cls):
        cls.program_counter = 0
        cls.accumulator = 0
