
def get_instructions(code):
    instructions = []
    instruction_count = 0
    for index, char in enumerate(code):
        if char.isupper():
            instructions.append((char, index))
            instruction_count += 1

    return instructions, instruction_count

def get_parameters(code):
    parameters = []
    for index, char in enumerate(code):
        if char.islower():
            parameters.append((char, index))
    return parameters


def get_nop_count(instructions, parameters):
    nop_count = 0
    for inst in instructions:
        if inst[1] % 4 != 0:
            nop_count += 4 - inst[1] % 4
    return nop_count


code = input()
instructions, instruction_count = get_instructions(code)
parameters = get_parameters(code)
nop_count = get_nop_count(instructions, parameters)
print(nop_count)
