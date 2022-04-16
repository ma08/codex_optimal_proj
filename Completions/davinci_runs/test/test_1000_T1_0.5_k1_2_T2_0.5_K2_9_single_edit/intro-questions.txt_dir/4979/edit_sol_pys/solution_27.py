

def reverse_binary(num):
    return int(str(bin(num))[2:][::-1], 2)

print(reverse_binary(int(input())))
