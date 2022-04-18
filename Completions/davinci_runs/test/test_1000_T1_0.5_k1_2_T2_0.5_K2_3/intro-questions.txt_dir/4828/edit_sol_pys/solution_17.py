

def main():
    program = input()
    num_nops = 0
    for i in range(len(program)):
        if i % 4 == 0 and program[i].islower():
            pass
        elif i % 4 == 0 and program[i].isupper():
            num_nops += 1
        elif i % 4 == 1 and program[i].isupper():
            num_nops += 1
        elif i % 4 == 1 and program[i].islower():
            pass
        elif i % 4 == 2 and program[i].isupper():
            num_nops += 2
        elif i % 4 == 2 and program[i].islower():
            pass
        elif i % 4 == 3 and program[i].islower():
            num_nops += 3
        elif i % 4 == 3 and program[i].isupper():
            pass
    print(num_nops)

main()
