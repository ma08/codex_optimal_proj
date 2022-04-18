

def convert_binary(num):
    octal = ""
    num = "0"*(3-len(num)%3) + num # add 0s to the front to make it divisible by 3
    for i in range(0, len(num), 3):
        octal += str(int(num[i:i+3], 2))
    return octal

print(convert_binary(input()))
