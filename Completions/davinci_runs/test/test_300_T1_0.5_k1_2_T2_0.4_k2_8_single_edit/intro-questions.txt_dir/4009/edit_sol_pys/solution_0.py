

n, x, y = map(int, input().split())
n = list(input())
print(n.count('0') if n[y] == '0' else n.count('0')+1)
