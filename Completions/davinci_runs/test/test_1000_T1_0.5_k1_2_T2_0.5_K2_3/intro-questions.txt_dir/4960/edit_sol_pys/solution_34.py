

def binary_to_octal(bin):
    bin = "0" * (3 - len(bin) % 3) + bin
    res = ""
    for i in range(0, len(bin), 3):
        res += str(int(bin[i:i+3], 2))
    return res

print(binary_to_octal(input()))
