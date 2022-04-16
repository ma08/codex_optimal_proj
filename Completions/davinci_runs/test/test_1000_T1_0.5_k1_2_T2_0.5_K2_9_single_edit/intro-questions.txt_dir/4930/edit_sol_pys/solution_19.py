

text = input("Enter text to decode: ")


def decode(text):
    decoded = ""
    for i in range(len(text)):
        if text[i] in "aeiou":
            decoded += text[i]
        elif text[i-1] in "aeiou":
            continue
        else:
            decoded += text[i]
    return decoded


print(decode(text))
