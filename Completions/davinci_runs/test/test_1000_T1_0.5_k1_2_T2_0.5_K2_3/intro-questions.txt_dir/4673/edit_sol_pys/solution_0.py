#!/usr/bin/env python3

import sys


def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def is_right(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def is_obtuse(a, b, c):
    return a ** 2 + b ** 2 < c ** 2


def is_acute(a, b, c):
    return a ** 2 + b ** 2 > c ** 2


def is_isosceles(a, b, c):
    return a == b or b == c or a == c


def is_equilateral(a, b, c):
    return a == b and b == c


def classify(a, b, c):
    if not is_triangle(a, b, c):
        return 'not a triangle'
    elif is_equilateral(a, b, c):
        return 'equilateral'
    elif is_isosceles(a, b, c):
        return 'isosceles'
    else:
        return 'scalene'


def main():
    for line in sys.stdin:
        a, b, c = map(int, line.split())
        print(classify(a, b, c))


if __name__ == '__main__':
    main()


def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
