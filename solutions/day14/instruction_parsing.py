import re


def parse_bitmask_instruction(instr):
    mask_value = instr.replace("mask = ", "")
    return mask_value


def parse_memory_assignment_instruction(instr):
    match = re.search(r'mem\[([0-9]+)] = ([0-9]+)', instr)
    return int(match.group(1)), int(match.group(2))
