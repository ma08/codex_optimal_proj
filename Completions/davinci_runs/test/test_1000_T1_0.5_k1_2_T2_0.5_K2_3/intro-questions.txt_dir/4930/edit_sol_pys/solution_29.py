
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

if __name__ == "__main__":
    text = input('Enter text: ')
    print(f'Decoded text: {decode(text)}')
