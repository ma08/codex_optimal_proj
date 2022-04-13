def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[0] in vowels:
        return word + "yay"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"


with open("file.txt") as f:
    for line in f:
        words = line.split()
        for word in words:
            print(pig_latin(word), end=" ")
        print()
