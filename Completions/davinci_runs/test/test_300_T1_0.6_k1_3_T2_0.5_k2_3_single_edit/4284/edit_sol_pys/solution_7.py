

#-------------------------------------------------------------------------------
# Name:        file
# Purpose:
#
# Author:      v.osipov@gmail.com
#
# Created:     16/10/2019
# Copyright:   (c) v.osipov 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from collections import Counter
def main():
    with open('file.txt', mode='w', encoding='utf-8') as f:
        text = f.write('Привет, мир!\nЭто мой первый файл.\n')
    with open('file.txt', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    with open('file.txt', encoding='utf-8') as f:
        text = f.read()
    print(text)
    print(len(text))
    print(text.count('Привет'))
    print(text.count('первый'))
    print(text.count('файл'))
    print(text.count('мир'))
    print(text.count('Привет'))
    print(text.count('первый'))
    print(text.count('файл'))
    print(text.count('мир'))
    c = Counter(text)
    print(c)

if __name__ == '__main__':
    main()
