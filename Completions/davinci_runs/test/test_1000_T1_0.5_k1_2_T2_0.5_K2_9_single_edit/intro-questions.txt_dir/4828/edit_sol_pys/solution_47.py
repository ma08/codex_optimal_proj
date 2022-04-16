

def main():
    program = input()
    num_nop = 0
    for i in range(len(program)):
        if i % 4 == 0 and program[i].isupper() or i % 4 == 1 and program[i].islower() or i % 4 == 2 and program[i].islower() or i % 4 == 3 and program[i].islower():
            pass
        elif i % 4 == 0 and program[i].islower() or i % 4 == 1 and program[i].isupper() or i % 4 == 2 and program[i].isupper() or i % 4 == 3 and program[i].isupper():
            num_nop += 1

    print(num_nop)

main()
