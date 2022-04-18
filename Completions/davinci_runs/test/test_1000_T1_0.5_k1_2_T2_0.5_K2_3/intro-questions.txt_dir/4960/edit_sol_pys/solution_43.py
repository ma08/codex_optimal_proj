

def binary_to_octal(binary_num):
    if len(binary_num) % 3 != 0:
        binary_num = "0"*(3-len(binary_num)%3) + binary_num
    res = ""
    for i in range(0, len(binary_num), 3):
        res += str(int(binary_num[i:i+3], 2))
    return res

print(binary_to_octal("10101100"))
