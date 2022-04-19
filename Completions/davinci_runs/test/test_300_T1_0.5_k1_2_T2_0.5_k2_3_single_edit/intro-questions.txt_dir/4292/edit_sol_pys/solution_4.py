
import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = [int(i) for i in sys.stdin.readline().split()]
prices.sort()


# https://www.hackerrank.com/challenges/mini-max-sum/problem
print(sum(prices[:k]))
