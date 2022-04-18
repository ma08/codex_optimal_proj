

def reverse_binary(num):
    return int(str(bin(num))[:1:-1], 2) # b[:1:-1] is the same as b[:-2:-1]

print(reverse_binary(int(input())))
