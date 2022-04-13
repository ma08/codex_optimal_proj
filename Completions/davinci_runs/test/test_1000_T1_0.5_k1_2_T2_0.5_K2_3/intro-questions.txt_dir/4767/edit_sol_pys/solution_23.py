
def main():
    registers = [int(x) for x in input().split()]
    max_val = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(len(registers) - 1, -1, -1):
        if registers[i] < max_val[i]:
            registers[i] += 1
            break
        else:
            registers[i] = 0
    print(sum(max_val) - sum(registers))


if __name__ == "__main__":
    main()
