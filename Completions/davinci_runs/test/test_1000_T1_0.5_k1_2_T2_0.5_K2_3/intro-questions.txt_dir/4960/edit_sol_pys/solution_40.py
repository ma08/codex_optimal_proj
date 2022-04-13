def octal_to_binary (n):
    binary = ''
    while n != 0:
        binary = str(n % 8) + binary
        n = n // 8
    return binary

binar = input()
print(octal_to_binary(int(binar)))
