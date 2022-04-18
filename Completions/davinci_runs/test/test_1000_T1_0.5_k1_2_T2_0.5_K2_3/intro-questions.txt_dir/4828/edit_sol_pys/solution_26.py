

def get_operations(code):
    operations = []
    operation_count = 0
    for index, char in enumerate(code):
        if char.isupper():
            operations.append((char, index))
            operation_count += 1
    return operations, operation_count

def get_parameters(code):
    parameters = []
    for index, char in enumerate(code):
        if char.islower():
            parameters.append((char, index))
    return parameters

def get_nop_count(operations, parameters):
    nop_count = 0
    for op in operations:
        if op[1] % 4 != 0:
            nop_count += 4 - op[1] % 4
    return nop_count

code = input()
operations, operation_count = get_operations(code)
parameters = get_parameters(code)
nop_count = get_nop_count(operations, parameters)
print(nop_count)
