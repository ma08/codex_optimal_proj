
text = input()
for i in range(1,len(text)):
    if text[i] == text[i-1]:
        text = text[:i] + text[i+1:]
        i -= 1

print(text)
