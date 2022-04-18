# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    for i, word in enumerate(words):
        for j, word2 in enumerate(words[i + 1:]):
            if word[-1] == word2[0]:
                break
        else:
            print(word)
            exit()

    print('correct')
