

def convert_binary(num):
    binary = ""
    num = "0"*(3 - len(num) % 3) + num
    for i in range(0, len(num), 3):
        binary += str(int(num[i:i + 3], 2))
    return binary


print(convert_binary(input()))
