

def divide(string):
    return string[:len(string)//2], string[len(string)//2:]

def rotate(string):
    total = 0
    for c in string:
        total += ord(c) - ord('A')
    return total

def merge(string1, string2):
    output = ""
    for i in range(len(string1)):
        output += chr((ord(string1[i]) - ord('A') + ord(string2[i]) - ord('A')) % 26 + ord('A'))
    return output

message = input()

a, b = divide(message)
a = rotate(a)
b = rotate(b)
print(merge(a, b))