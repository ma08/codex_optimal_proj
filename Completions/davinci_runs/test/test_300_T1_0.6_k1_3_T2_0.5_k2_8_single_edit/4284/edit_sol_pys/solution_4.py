

#-------------------------------------------------------------------------------
# Name:        file
# Purpose:     Пример открытия файла
#
# Author:      v.osipov (v.osipov@yandex.ru)
#
# Created:     16/10/2018
# Copyright:   (c) v.osipov 2018-2019


import os

# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

def open_file(filename, mode):
    """Открытие файла"""
    try:
        f = open(filename, mode)
    except IOError as e:
        print("Невозможно открыть файл", filename, "Режим", mode)
        print(e)
        return None
    else:
        return f


def read_file(f):
    """Чтение файла"""
    try:
        return f.read()
    except IOError as e:
        print("Невозможно прочитать файл")
        print(e)
        return None


def close_file(f):
    """Закрытие файла"""
    try:
        f.close()
    except IOError as e:
        print("Невозможно закрыть файл")
        print(e)
        return None


def test_file(filename):
    """Тестирование файла"""
    f = open_file(filename, "r")
    if f is not None:
        data = read_file(f)
        if data is not None:
            print(data)
        close_file(f)


def test_file_with(filename):
    """Тестирование файла с использованием конструкции with"""
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")


    pass

    test_file("data.txt")
    test_file_with("data.txt")
if __name__ == '__main__':
    main()
