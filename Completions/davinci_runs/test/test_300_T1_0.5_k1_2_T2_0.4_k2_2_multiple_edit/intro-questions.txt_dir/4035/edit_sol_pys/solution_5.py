

import unittest

def main(A, B):
    return B // A if B % A == 0 else -1

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(2, 2), 1)
        self.assertEqual(main(8, 9), -1)

if __name__ == '__main__':
    unittest.main()
