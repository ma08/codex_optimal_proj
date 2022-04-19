

import unittest
import math

def main(A, B):
    if A % B == 0:
        return A // B
    else:
        return -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(25, 5), 5)
        self.assertEqual(main(8, 9), -1)

if __name__ == '__main__':
    unittest.main()
