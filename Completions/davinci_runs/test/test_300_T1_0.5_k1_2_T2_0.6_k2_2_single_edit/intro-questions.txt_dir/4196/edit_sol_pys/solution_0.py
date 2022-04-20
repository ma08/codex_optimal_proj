# -*- coding: utf-8 -*-


import sys
from io import StringIO
import unittest


def resolve():
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    n = int(input())
    a_list = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, gcd(a_list[i], a_list[j]))

    print(ans)


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
        input = """3
5 7 10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 8 8 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
27 16 9 8 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
