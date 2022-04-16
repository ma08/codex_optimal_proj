

def rotate(string):
    return sum(ord(c) - ord('A') for c in string)

def merge(string1, string2):
    return "".join(chr((ord(string1[i]) - ord('A') + ord(string2[i]) - ord('A')) % 26 + ord('A')) for i in range(len(string1)))

message = input()

a, b = divide(message)
a = rotate(a)
b = rotate(b)
print(merge(a, b))
