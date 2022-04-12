

def reverse_binary(n):
    return int(str(bin(n))[:1:-1], 2)

print(reverse_binary(int(input())))
