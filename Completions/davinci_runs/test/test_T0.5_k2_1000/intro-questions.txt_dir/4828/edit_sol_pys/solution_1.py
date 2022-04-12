
def get_instructions(code):
    instructions = []
    for index, char in enumerate(code):
        if char.isupper():
            instructions.append((char, index))
    return instructions

def get_parameters(code):
    parameters = []
    for index, char in enumerate(code):
        if char.islower():
            parameters.append((char, index))
    return parameters

def get_nop_count(instructions):
    nop_count = 0
    for inst in instructions:
        if inst[1] % 4 != 0:
            nop_count += 4 - inst[1] % 4
    return nop_count

code = input()
instructions = get_instructions(code)
parameters = get_parameters(code)
nop_count = get_nop_count(instructions)
print(nop_count)
