

def reverse_binary(n):
    return int(bin(n)[2:][::-1], 2) # bin(n)[2:] removes the 0b

print(reverse_binary(int(input())))
