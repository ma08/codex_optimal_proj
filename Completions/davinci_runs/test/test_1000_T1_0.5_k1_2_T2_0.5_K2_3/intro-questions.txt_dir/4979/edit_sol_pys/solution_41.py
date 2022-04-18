

def reverse_bin(n: int) -> int:
    return int(bin(int(n, 2))[2:][::-1], 2)

print(reverse_bin(input()))
