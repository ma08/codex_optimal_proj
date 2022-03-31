

import unittest

from typing import List

from utils.common import ListNode


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.maxProfit([]), 0)

    def test_one(self):
        self.assertEqual(self.sol.maxProfit([1]), 0)
        self.assertEqual(self.sol.maxProfit([2]), 0)

    def test_two(self):
        self.assertEqual(self.sol.maxProfit([2, 1]), 0)
        self.assertEqual(self.sol.maxProfit([1, 2]), 1)

    def test_three(self):
        self.assertEqual(self.sol.maxProfit([1, 3, 2]), 2)

    def test_general(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.sol.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()