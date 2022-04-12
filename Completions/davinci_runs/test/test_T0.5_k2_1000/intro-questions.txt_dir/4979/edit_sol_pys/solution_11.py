

def reverse_bin(n: int) -> int:
    return int(bin(n)[2:][::-1], 2)  # [2:] to remove 0b prefix

if __name__ == "__main__":
    print(reverse_bin(int(input())))
