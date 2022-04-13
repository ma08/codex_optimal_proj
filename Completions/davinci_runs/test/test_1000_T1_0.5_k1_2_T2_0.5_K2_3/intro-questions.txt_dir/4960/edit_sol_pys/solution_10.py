

def binary_to_octal(binary_number):
    binary_number = "0" * (3 - len(binary_number) % 3) + binary_number
    res = ""
    for i in range(0, len(binary_number), 3):
        res += str(int(binary_number[i:i + 3], 2))
    return res


print(binary_to_octal(input()))
