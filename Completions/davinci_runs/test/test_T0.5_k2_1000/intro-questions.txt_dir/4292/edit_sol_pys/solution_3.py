
import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
price = [int(i) for i in sys.stdin.readline().split()]
price.sort()

print(sum(price[:k]))
