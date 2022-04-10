
import unittest
import sys
import random

class HashMap:
    def __init__(self):
        self.hash_map_ = {}
        self.size = 0

    def get(self, key):
        return self.hash_map_[key]

    def put(self, key, value):
        self.size += 1
        self.hash_map_[key] = value

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def contains_key(self, key):
        return key in self.hash_map_

    def contains_value(self, value):
        return value in self.hash_map_.values()

    def remove(self, key):
        del self.hash_map_[key]

    def clear(self):
        self.hash_map_ = {}
        self.size = 0

    def key_set(self):
        return self.hash_map_.keys()

    def value_set(self):
        return self.hash_map_.values()


def calc_prefix_sum(array):
    prefix_sum = [0]
    size = len(array)

    for i in range(size):
        prefix_sum.append(prefix_sum[i] + array[i])

    return prefix_sum


def find_max_sum_of_beauty(n, k, x, array):
    prefix_sum = calc_prefix_sum(array)

    hash_map_ = HashMap()
    hash_map_.put(0, 0)
    hash_map_.put(1, prefix_sum[k])

    for i in range(x, n + 1):
        for j in range(max(1, i - k), min(i, x) + 1):
            hash_map_.put(i, max(hash_map_.get(i), hash_map_.get(i - j) + prefix_sum[i] - prefix_sum[i - j]))

    if hash_map_.contains_key(n):
        return hash_map_.get(n)
    else:
        return -1


class Test(unittest.TestCase):
    def test_find_max_sum_of_beauty(self):
        self.assertEqual(find_max_sum_of_beauty(5, 2, 3, [5, 1, 3, 10, 1]), 18)
        self.assertEqual(find_max_sum_of_beauty(6, 1, 5, [10, 30, 30, 70, 10, 10]), -1)
        self.assertEqual(find_max_sum_of_beauty(4, 3, 1, [1, 100, 1, 1]), 100)


def main():
    n, k, x = map(int, input().split(' '))
    array = list(map(int, input().split(' ')))
    print(find_max_sum_of_beauty(n, k, x, array))


if __name__ == '__main__':
    main()
