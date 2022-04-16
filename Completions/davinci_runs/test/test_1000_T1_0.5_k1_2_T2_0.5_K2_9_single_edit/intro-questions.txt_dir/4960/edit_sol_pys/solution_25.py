
def binary_to_octal(binary):
    binary = "0"*(3-len(binary)%3) + binary
    res = ""
    for i in range(0, len(binary), 3):
        res += str(int(binary[i:i+3], 2))
    return res


if __name__ == "__main__":
    print(binary_to_octal(input()))
