

text = input()

def decode(text):
    decoded = ""
    for i in range(len(text)):
        if text[i] in "aeiou":
            decoded += text[i]
        elif i >= 1 and text[i-1] in "aeiou":
            continue
        else:
            decoded += text[i]
    return decoded

print(decode(text))
