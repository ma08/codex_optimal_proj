

def solve(string, k):
	n = len(string)
	i = 0
	while i < n and string[i] == string[0]:
		i += 1
	if i == n:
		return string * (k // n) + string[:k % n]
	else:
		return string * k

n, k = map(int, input().split())
string = input()
print(solve(string, k))
