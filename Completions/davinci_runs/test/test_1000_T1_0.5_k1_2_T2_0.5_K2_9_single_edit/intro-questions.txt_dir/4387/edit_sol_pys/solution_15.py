#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main():
    r = int(input())
    if r < 1200:
        print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == '__main__':
    main()


def test_main():
    assert main() == (
        'ABC',
        'ARC',
        'AGC',
    )


def resolve():
    r = int(input())
    if r < 1200:
        print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")


import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1199"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1200"""
        output = """ARC"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4208"""
        output = """AGC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1199"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1200"""
        output = """ARC"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4208"""
        output = """AGC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    r = int(input())
    if r < 1200:
    print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")
