

def reverse_binary(n):
    return int(bin(n)[2:][::-1], 2)

print(reverse_binary(int(input())))
