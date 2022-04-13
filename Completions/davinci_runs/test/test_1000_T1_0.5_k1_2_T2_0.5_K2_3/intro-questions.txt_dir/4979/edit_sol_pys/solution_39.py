
def reverse_binary(n):
    return int(bin(n)[2:][::-1], 2)  # I'm not sure if this is what they want.

if __name__ == "__main__":
    print(reverse_binary(int(input())))
