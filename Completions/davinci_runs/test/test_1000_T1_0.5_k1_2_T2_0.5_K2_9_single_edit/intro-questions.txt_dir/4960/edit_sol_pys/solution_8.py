

def convert_binary(num):
    octal = ""
    num = "0"*(4-len(num)%4) + num
    for i in range(0, len(num), 4):
        octal += str(int(num[i:i+4], 2))
    return octal

print(convert_binary(input()))
