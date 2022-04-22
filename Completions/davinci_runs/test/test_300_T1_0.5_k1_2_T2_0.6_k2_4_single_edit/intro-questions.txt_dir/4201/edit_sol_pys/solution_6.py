

n = int(input())
s = input()

s = s.replace('BC', 'D')

ans = 0
cnt = 0
for c in s:
	if c == 'A':
		cnt += 1
	elif c == 'D':
		ans += cnt
	else:
		cnt = 0

print(ans)
