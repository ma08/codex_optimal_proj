

import unittest
import math

class Main:
    def main(self, A, B):
        if B % A == 0:
            return B // A
        else:
            return -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(Main.main(2, 2), 1)
        self.assertEqual(Main.main(8, 9), -1)

if __name__ == '__main__':
    unittest.main()
