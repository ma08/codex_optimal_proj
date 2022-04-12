

def reverse_binary(n): # reverse binary number
    return int(bin(n)[2:][::-1], 2) # [2:] to remove 0b, [::-1] to reverse

print(reverse_binary(int(input())))
