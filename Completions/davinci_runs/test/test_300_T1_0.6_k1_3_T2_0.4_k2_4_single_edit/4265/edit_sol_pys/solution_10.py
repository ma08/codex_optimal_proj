

# https://atcoder.jp/contests/abc085/tasks/abc085_a

n = int(input())
s = input()
t = input()

count = 0
for i in range(n):
	if s[i] != t[i]:
		count += 1

print(count)
