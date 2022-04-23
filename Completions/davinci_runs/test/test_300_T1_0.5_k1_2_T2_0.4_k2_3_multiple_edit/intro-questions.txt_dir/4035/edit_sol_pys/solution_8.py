

import unittest


def solution(A, B):
    if B % A == 0:
        return B // A
    else:
        return -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solution(2, 2), 1)
        self.assertEqual(solution(8, 9), -1)

if __name__ == '__main__':
    unittest.main()
