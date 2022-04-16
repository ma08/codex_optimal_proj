

text = input()

def decode(text):
    decoded = ""
    for i in range(len(text)):
        if text[i] in "aeiou":
            decoded += text[i]
        else:
            decoded += text[i]
    return decoded

print(decode(text))
