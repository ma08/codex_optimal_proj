

import unittest

def main(A, B):
    if B % A == 0:
        return B // A
    else:
        return -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(2, 4), 2)
        self.assertEqual(main(8, 9), -1)

if __name__ == '__main__':
    unittest.main()
