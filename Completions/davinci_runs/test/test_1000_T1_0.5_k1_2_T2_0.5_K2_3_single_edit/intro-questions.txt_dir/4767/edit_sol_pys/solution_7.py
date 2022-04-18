
def main():
    registers = [int(x) for x in input().split()]
    max_val = [2, 3, 5, 7, 11, 13, 17, 19]  # prime numbers
    for i in range(len(registers) - 1, -1, -1):
        if registers[i] < max_val[i] - 1:  # prime numbers
            registers[i] += 1
            break
        else:
            registers[i] = 0
    print(sum(max_val) - sum(registers))


if __name__ == "__main__":
    main()
