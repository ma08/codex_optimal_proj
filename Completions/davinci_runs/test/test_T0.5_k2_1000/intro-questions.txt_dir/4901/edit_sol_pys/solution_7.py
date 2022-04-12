
def divide(text):
    return text[:len(text) // 2], text[len(text) // 2:]


def rotate(text):
    total = 0
    for c in text:
        total += ord(c) - ord('A')

    return total

def merge(text1, text2):
    output = ""
    for i in range(len(text1)):
        output += chr((ord(text1[i]) - ord('A') + ord(text2[i]) - ord('A')) % 26 + ord('A'))
    return output

message = input()

a, b = divide(message)
a = rotate(a)
b = rotate(b)
print(merge(a, b))
