from sys import stdin

word = input()
perm = input()

print("YES" if all(map(lambda x: x in perm, word)) else "NO", file = stdin)
