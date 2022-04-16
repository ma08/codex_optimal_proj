

letters = [0 for i in range(26)]  # массив из 26 нулей

for letter in input():
    letters[ord(letter) - ord('a')] += 1  # находим индекс буквы в массиве

print(sum(letter % 2 for letter in letters))  # проверяем на нечетность
