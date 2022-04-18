
# -*- coding: utf-8 -*-
# @Author: Joe
# @Date:   2017-05-26 15:39:49
# @Last Modified by:   Joe
# @Last Modified time: 2017-05-26 15:41:38
import sys

def main():
    sentence = sys.stdin.readline().strip()
    word = ''
    decoded_sentence = ''

    for letter in sentence:
        if letter == ' ':
            if word != '':
                decoded_sentence += word + ' '
                word = ''
        else:
            if letter == 'p':
                word += letter
            else:
                word += letter + 'p' + letter

    if word != '':
        decoded_sentence += word

    print(decoded_sentence)

if __name__ == '__main__':
    main()
