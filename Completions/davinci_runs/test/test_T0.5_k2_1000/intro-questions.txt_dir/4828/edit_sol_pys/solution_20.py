

def get_instructions(code, instruction_count):
    instructions = []
    for index, char in enumerate(code):
        if char.isupper():
            instructions.append((char, index))
    return instructions

def get_parameters(code, instruction_count):
    parameters = []
    for index, char in enumerate(code[:instruction_count]):
        if char.islower():
            parameters.append((char, index))
    return parameters

def get_nop_count(instructions, instruction_count):
    nop_count = 0 
    for inst in instructions[:instruction_count]:
        if inst[1] % 4 != 0:
            nop_count += 4 - inst[1] % 4
    return nop_count

code = input()
instruction_count = int(input())
instructions = get_instructions(code, instruction_count)
parameters = get_parameters(code, instruction_count)
nop_count = get_nop_count(instructions, instruction_count)
print(nop_count)
