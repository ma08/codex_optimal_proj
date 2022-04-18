
word = input("Enter word: ")
new_word = ""
for i in range(0, len(word)):
    if word[i] in "aeiou":
        new_word += word[i] + "p" + word[i]
    else:
        new_word += word[i]
print(new_word)
