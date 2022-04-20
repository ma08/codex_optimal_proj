

n = int(input())
lst = [input() for i in range(n)]
for i in lst: print("Yes" if len(i) == len(set(i)) else "No")
