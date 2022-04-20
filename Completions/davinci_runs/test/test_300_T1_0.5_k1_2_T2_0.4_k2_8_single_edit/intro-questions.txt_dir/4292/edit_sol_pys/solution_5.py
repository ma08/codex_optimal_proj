
import sys

n, k = [int(i) for i in sys.stdin.readline().split()] # n, k 입력
prices = [int(i) for i in sys.stdin.readline().split()] # 가격 입력
prices.sort() # 정렬

print(sum(prices[:k]))
