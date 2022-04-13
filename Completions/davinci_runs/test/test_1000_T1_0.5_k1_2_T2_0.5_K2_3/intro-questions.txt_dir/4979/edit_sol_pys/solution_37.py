

def reverse_binary(num):
    return int(str(bin(num))[:1:-1], 2)

print(reverse_binary(int(input())))
