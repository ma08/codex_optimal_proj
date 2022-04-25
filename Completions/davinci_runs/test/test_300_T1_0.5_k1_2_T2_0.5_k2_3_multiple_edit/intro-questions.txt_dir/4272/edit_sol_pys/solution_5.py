# https://atcoder.jp/contests/abc176/tasks/abc176_a

s = input()
n = int(input())

count = 0

for i in range(n - 2):
    if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
        count += 1

print(count)
