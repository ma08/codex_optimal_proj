

def binary_to_octal(binary):
    binary = binary[::-1]
    binary = binary + (3 - len(binary) % 3) * '0'
    octal = ''
    for i in range(0, len(binary), 3):
        octal += str(int(binary[i:i + 3], 2))

    return int(octal[::-1])

print(binary_to_octal('101'))
