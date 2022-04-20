

import sys

n = int(input())
s = input()

def shift_character(char, shift):
    """
    :param char: a single character
    :param shift: number of shifts to make
    :return: the shifted character
    """
    return chr(ord(char) + shift)

def shift_string(string, shift):
    """
    :param string: a string of characters
    :param shift: number of shifts to make
    :return: the shifted string
    """
    return ''.join([shift_character(char, shift) for char in string])

def wrap_around(string):
    """
    :param string: a string of characters
    :return: a string of characters with the last character wrapped around to the front
    """
    return string[-1] + string[:-1]

def wrap_around_shift(string, shift):
    """
    :param string: a string of characters
    :param shift: number of shifts to make
    :return: a string of characters with the last character wrapped around to the front, then shifted
    """
    return shift_string(wrap_around(string), shift)

def wrap_around_shift_string(string, shift):
    """
    :param string: a string of characters
    :param shift: number of shifts to make
    :return: a string of characters with each character wrapped around to the front, then shifted
    """
    return ''.join([wrap_around_shift(char, shift) for char in string])

sys.stdout.write(wrap_around_shift_string(s, n))