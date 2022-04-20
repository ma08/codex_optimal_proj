
# Задача на программирование: расстояние Левенштейна
# https://www.coursera.org/learn/dynamic-programming-decomposition/programming/UiY6U/rasstoianie-lievienstieina

import numpy as np


def levenshtein_distance(str1, str2):
    n, m = len(str1), len(str2)
    D = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        D[i, 0] = i
    for j in range(m + 1):
        D[0, j] = j

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                D[i, j] = D[i - 1, j - 1]
            else:
                D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + 1)

    return int(D[n, m])


str1 = input()
str2 = input()

print(levenshtein_distance(str1, str2))


# Задача на программирование: обработка текста
# https://www.coursera.org/learn/dynamic-programming-decomposition/programming/z8jYW/obrabotka-tiaksta

import sys


def get_words(text):
    words = []
    word = []

    for symbol in text:
        if symbol.isalpha():
            word.append(symbol)
        elif word:
            words.append(''.join(word))
            word = []

    if word:
        words.append(''.join(word))

    return words


def get_sentences(text):
    sentences = []
    sentence = []

    for symbol in text:
        if symbol == '.' or symbol == '!' or symbol == '?':
            sentence.append(symbol)
            sentences.append(''.join(sentence))
            sentence = []
        else:
            sentence.append(symbol)

    return sentences


def get_statistics(words, sentences):
    words_count = len(words)
    sentences_count = len(sentences)

    if words_count == 0:
        return 0, 0

    words_per_sentence = words_count / sentences_count
    letters_per_word = sum([len(word) for word in words]) / words_count

    return words_per_sentence, letters_per_word


def main():
    text = sys.stdin.read()

    words = get_words(text)
    sentences = get_sentences(text)

    words_per_sentence, letters_per_word = get_statistics(words, sentences)

    print(words_per_sentence)
    print(letters_per_word)


if __name__ == '__main__':
    main()


# Задача на программирование: проекты
# https://www.coursera.org/learn/dynamic-programming-decomposition/programming/YXyV7/proiekty

# 1st solution

n, r = map(int, input().split())

projects = []
for i in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

projects.sort(key=lambda x: x[0])

count = 0
for i in range(n):
    if projects[i][0] <= r:
        r += projects[i][1]
        count += 1
    else:
        break

print(count)

# 2nd solution

"""
# Решение в стиле динамики

n, r = map(int, input().split())

projects = []
for i in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

projects.sort(key=lambda x: x[0])

dp = [0] * (r + 1)

for i in range(n):
    for j in range(r, projects[i][0] - 1, -1):
        if dp[j] < dp[j - projects[i][0]] + projects[i][1] and j - projects[i][0] >= 0:
            dp[j] = dp[j - projects[i][0]] + projects[i][1]

print(dp[r])
"""
