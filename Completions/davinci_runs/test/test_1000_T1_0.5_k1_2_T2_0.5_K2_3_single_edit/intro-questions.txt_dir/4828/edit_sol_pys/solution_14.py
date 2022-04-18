

def main():
    program = input()
    num_nop = 0
    for i in range(len(program)):
        if i % 4 == 0 and program[i].isupper():
            pass
        if i % 4 == 0 and program[i].islower():
            num_nop += 1
        if i % 4 == 1 and program[i].isupper():
            num_nop += 1
        if i % 4 == 1 and program[i].islower():
            pass
        if i % 4 == 2 and program[i].isupper():
            num_nop += 2
        if i % 4 == 2 and program[i].islower():
            pass
        if i % 4 == 3 and program[i].isupper():
            num_nop += 3
        if i % 4 == 3 and program[i].islower():
            pass
    print(num_nop)

main()
