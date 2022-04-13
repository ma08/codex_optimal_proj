

def convert_binary(num):
    decimal = ""
    num = "0"*(3 - len(num)%3) + num
    for i in range(0, len(num), 3):
        decimal += str(int(num[i:i+3], 2))
    return decimal

print(convert_binary(input()))
