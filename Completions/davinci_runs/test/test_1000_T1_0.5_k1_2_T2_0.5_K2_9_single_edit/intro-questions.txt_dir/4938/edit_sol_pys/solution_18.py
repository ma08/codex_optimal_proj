
# Посчитать сколько раз встречается каждое слово в файле

text = open("text.txt", "r", encoding="utf-8").read()
text = text.lower()

words = text.split()

words_d = {}

for word in words:
    if word in words_d:
        words_d[word] += 1
    else:
        words_d[word] = 1

for word in words_d:
    print(word, words_d[word])

# Сколько слов в файле?

print(len(words_d))

# Сколько букв в файле?

letters = 0

for letter in text:
    if letter.isalpha():
        letters += 1

print(letters)

# Отсортировать слова по алфавиту

for word in sorted(words_d):
    print(word)

# Отсортировать слова по длине

for word in sorted(words_d, key=len):
    print(word)

# Отсортировать слова по частоте использования

for word in sorted(words_d, key=words_d.get):
    print(word, words_d[word])

# Отсортировать буквы по частоте использования

letters_d = {}

for letter in text:
    if letter.isalpha():
        if letter in letters_d:
            letters_d[letter] += 1
        else:
            letters_d[letter] = 1

for letter in sorted(letters_d, key=letters_d.get):
    print(letter, letters_d[letter])

# Посчитать сколько слов в файле начинается на гласную

vowels = 'аеёиоуыэюя'

vowels_words = 0

for word in words_d:
    if word[0] in vowels:
        vowels_words += 1

print(vowels_words)

# Посчитать сколько слов в файле начинается на согласную

consonants = 'бвгджзйклмнпрстфхцчшщ'

consonants_words = 0

for word in words_d:
    if word[0] in consonants:
        consonants_words += 1

print(consonants_words)

# Посчитать сколько букв в файле является гласными

vowels_letters = 0

for letter in letters_d:
    if letter in vowels:
        vowels_letters += letters_d[letter]

print(vowels_letters)

# Посчитать сколько букв в файле является согласными

consonants_letters = 0

for letter in letters_d:
    if letter in consonants:
        consonants_letters += letters_d[letter]

print(consonants_letters)

# Посчитать сколько слов в файле состоит из одной буквы

one_letter_words = 0

for word in words_d:
    if len(word) == 1:
        one_letter_words += 1

print(one_letter_words)

# Сколько слов в файле заканчивается на гласную

vowels_words_2 = 0

for word in words_d:
    if word[-1] in vowels:
        vowels_words_2 += 1

print(vowels_words_2)

# Сколько слов в файле заканчивается на согласную

consonants_words_2 = 0

for word in words_d:
    if word[-1] in consonants:
        consonants_words_2 += 1

print(consonants_words_2)

# Посчитать сколько букв в файле является гласными и заканчивается на гласную

vowels_letters_2 = 0

for letter in letters_d:
    if letter in vowels and letter[-1] in vowels:
        vowels_letters_2 += letters_d[letter]

print(vowels_letters_2)

# Посчитать сколько букв в файле является согласными и заканчивается на согласную

consonants_letters_2 = 0

for letter in letters_d:
    if letter in consonants and letter[-1] in consonants:
        consonants_letters_2 += letters_d[letter]

print(consonants_letters_2)

# Сколько букв в файле не является гласными и не заканчивается на гласную

non_vowels_letters = 0

for letter in letters_d:
    if letter not in vowels and letter[-1] not in vowels:
        non_vowels_letters += letters_d[letter]

print(non_vowels_letters)

# Сколько букв в файле н

X = int(input())
line = input()

women = men = 0

for person in line:
    if person == 'W':
        women += 1
    else:
        men += 1

    if abs(women - men) > X:
        break

print(women + men)
