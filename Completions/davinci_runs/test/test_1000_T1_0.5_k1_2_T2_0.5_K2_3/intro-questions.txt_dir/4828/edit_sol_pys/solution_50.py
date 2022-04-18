

def get_instructions(code):
    instructions = []
    instruction_count = 0
    for index, char in enumerate(code):
        if char.isupper():
            instructions.append((char, index))
            instruction_count += 1
    return instructions, instruction_count

def get_registers(code):
    registers = []
    for index, char in enumerate(code):
        if char.islower():
            registers.append((char, index))
    return registers

def get_nop_count(instructions, registers):
    nop_count = 0
    for inst_index in instructions:
        if inst_index % 4 != 0:
            nop_count += 4 - inst_index % 4
    return nop_count

code = input()
instructions, instruction_count = get_instructions(code)
registers = get_registers(code)
nop_count = get_nop_count(instructions, registers)
print(nop_count)
