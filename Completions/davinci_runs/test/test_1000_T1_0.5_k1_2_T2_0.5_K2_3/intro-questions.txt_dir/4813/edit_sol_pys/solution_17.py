

word = input()  # Слово для отгадывания
permutation = input()  # Перестановка букв, которую вводит игрок
word_dict = {}  # Словарь с буквами и их количеством в оригинальном слове
for letter in word:
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1

guesses_left = 10  # Количество ошибок, которые может совершить игрок
for letter in permutation:
    if letter in word_dict:
        word_dict[letter] -= 1
        if word_dict[letter] == 0:
            word_dict.pop(letter)
            if len(word_dict) == 0:
                print('WIN')
                break
    else:
        guesses_left -= 1
        if guesses_left == 0:
            print('LOSE')
            break
