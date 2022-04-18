

def reverse_binary(n):  # convert to binary, remove 0b prefix, reverse, convert to integer
    return int(bin(n)[2:][::-1], 2)  # bin(n)[2:] removes 0b prefix, [::-1] reverses, int(, 2) to integer

if __name__ == "__main__":
    print(reverse_binary(int(input())))  # int(input()) converts input to integer
