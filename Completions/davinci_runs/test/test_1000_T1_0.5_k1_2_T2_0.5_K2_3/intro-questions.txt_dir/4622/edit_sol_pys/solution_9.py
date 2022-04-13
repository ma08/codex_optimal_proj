
import sys

n = int(input())
a_list = list(map(int, sys.stdin.readline().split()))

if len(set(a_list)) == n:  # set() 으로 중복을 제거하여 리스트의 길이와 같은지 비교
    print("YES")
else:
    print("NO")
