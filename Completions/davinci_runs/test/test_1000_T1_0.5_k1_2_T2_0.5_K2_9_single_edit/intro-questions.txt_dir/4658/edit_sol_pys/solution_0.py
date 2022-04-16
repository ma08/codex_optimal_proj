#!/usr/bin/env python3

from typing import List


def reverseBits(n: int) -> int:
    # n is binary string of length 32
    bin_str = bin(n)[2:]
    bin_str = bin_str.zfill(32)
    bin_str = bin_str[::-1]
    return int(bin_str, 2)


def findNumbers(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


def main():
    print(findNumbers([555, 901, 482, 1771]))


if __name__ == "__main__":
    main()
