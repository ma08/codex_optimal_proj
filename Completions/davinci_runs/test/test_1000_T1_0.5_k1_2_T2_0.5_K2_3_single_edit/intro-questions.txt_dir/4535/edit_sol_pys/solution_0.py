#!/usr/bin/env python3

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
