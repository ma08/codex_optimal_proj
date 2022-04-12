

def reverse_binary(number):
    return int(str(bin(number))[2:][::-1], 2)

print(reverse_binary(int(input())))
