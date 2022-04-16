

def reverse_binary(n: int) -> int:
    return int(bin(n)[2:][::-1], base=2)

if __name__ == "__main__":
    print(reverse_binary(int(input())))
