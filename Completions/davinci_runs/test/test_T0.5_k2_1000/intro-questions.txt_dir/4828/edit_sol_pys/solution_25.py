

def main():
    program = input()
    num_nop = 0 # number of NOP
    for i in range(len(program)):
        if i % 4 == 0 and program[i].isupper(): # if the first character is uppercase
            pass
        elif i % 4 == 0 and program[i].islower(): # if the first character is lowercase
            num_nop += 1
        elif i % 4 == 1 and program[i].isupper(): # if the second character is uppercase
            num_nop += 1
        elif i % 4 == 1 and program[i].islower(): # if the second character is lowercase
            pass
        elif i % 4 == 2 and program[i].isupper(): # if the third character is uppercase
            num_nop += 2
        elif i % 4 == 2 and program[i].islower(): # if the third character is lowercase
            pass
        elif i % 4 == 3 and program[i].isupper(): # if the fourth character is uppercase
            num_nop += 3
        elif i % 4 == 3 and program[i].islower():
            pass
    print(num_nop)

main()
