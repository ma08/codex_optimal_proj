

import unittest


def main(a, b):
    if b % a == 0:
        return b // a
    return -1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main(2, 4), 2)
        self.assertEqual(main(8, 9), -1)


if __name__ == '__main__':
    unittest.main()
