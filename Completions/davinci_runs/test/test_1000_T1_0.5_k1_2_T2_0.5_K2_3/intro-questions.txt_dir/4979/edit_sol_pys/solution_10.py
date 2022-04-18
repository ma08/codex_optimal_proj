

def reverse_bin(n: int) -> int:
    return int(bin(n)[2:][::-1], 2) # bin(n) -> returns 0b0 + binary number

print(reverse_bin(int(input())))
