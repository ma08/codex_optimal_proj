# -----Answer-----
# k = int(input())
# s = str(input())
# print(s[:k] + '...' if len(s) > k else s)


print(input()[:int(input())] + '...' if len(input()) > int(input()) else input())
