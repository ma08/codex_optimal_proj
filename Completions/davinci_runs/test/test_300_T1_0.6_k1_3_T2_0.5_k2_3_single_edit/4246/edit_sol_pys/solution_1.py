
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
 
def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print(sum(l[0:k]))
 
class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """5 3
50 100 80 120 80"""
        output = """210"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
1000"""
        output = """1000"""
        self.assertIO(input, output)
 
if __name__ == "__main__":
    unittest.main()
