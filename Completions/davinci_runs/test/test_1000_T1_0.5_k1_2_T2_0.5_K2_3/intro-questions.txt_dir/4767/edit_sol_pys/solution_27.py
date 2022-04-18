

def main():
    """
    Read in the current state of the registers.
    """
    registers = [int(i) for i in input().split()]

    """
    First, find the first non-zero register.
    """
    first_non_zero = 0
    for i in range(len(registers)):
        if registers[i] != 0:
            first_non_zero = i
            break

    """
    If the first non-zero register is the last register, then the number of
    operations that can be performed is the difference between the register
    value and the register size.
    """
    if first_non_zero == len(registers) - 1:
        print(19 - registers[first_non_zero])
        return

    """
    Otherwise, the number of operations that can be performed is the product of
    the register sizes of all registers following the first non-zero
    register.
    """
    print(reduce(lambda x, y: x * y, [19 - registers[i] for i in range(first_non_zero + 1, len(registers))]))

main()
