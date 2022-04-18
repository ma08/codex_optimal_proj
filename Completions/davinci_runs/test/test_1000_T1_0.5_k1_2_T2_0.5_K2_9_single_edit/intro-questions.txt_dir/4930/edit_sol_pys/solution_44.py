

text = input("Enter text: ")

def decode(text):
    decoded = ""
    for i in range(len(text)-1):
        if text[i] not in "aeiou":
            if text[i+1] not in "aeiou":
                decoded += text[i]
            else:
                continue
        elif text[i] in "aeiou":
            decoded += text[i] 
    return decoded

print(decode(text))
