

import unittest
import math

def main(A, B):
    if B % A != 0:
    return B // A

        return -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(2, 2), 25)
        self.assertEqual(main(8, 9), -1)


if __name__ == '__main__':
    unittest.main()
