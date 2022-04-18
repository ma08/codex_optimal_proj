

def get_directives(code):
    directives = []
    directive_count = 0
    for index, char in enumerate(code):
        if char.isupper():
            directives.append((char, index))
            directive_count += 1
    return directives, directive_count

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
directives, directive_count = get_directives(code)
parameters = get_parameters(code)
nop_count = get_nop_count(directives, parameters)
print(nop_count)
