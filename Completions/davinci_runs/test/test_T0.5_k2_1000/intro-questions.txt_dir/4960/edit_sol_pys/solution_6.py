

def convert_octal(num):
    octal = ""
    num = "0"*(3-len(num) % 3) + num
    for i in range(0, len(num), 3):
        octal += str(int(num[i:i+3], 2))
    return octal

print(convert_octal(input()))
