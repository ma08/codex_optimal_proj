
n = int(input())
s = input()

ans = n - sum(s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')

print(ans)
