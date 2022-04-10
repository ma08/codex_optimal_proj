

#from collections import defaultdict

def solve(s, b):
	#print("s: ", s)
	#print("b: ", b)
	#print("")
	res = []
	if len(b) == 0:
		return s
	if len(s) == 0:
		return ""
	for i in range(len(s)):
		if s[i] == 'a':
			continue
		b[0] -= (len(s) - i)
		b[i] -= i
		#print("i: ", i)
		#print("b: ", b)
		if b[0] >= 0 and b[i] >= 0:
			#print("b: ", b)
			#print("s[:i]: ", s[:i])
			#print("s[i+1:]: ", s[i+1:])
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("s[:i] + s[i+1:]: ", s[:i] + s[i+1:])
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("b[1:]: ", b[1:])
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("solve(s[:i] + s[i+1:], b[1:]): ", solve(s[:i] + s[i+1:], b[1:]))
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("s[i] + solve(s[:i] + s[i+1:], b[1:]): ", s[i] + solve(s[:i] + s[i+1:], b[1:]))
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("res.append(s[i] + solve(s[:i] + s[i+1:], b[1:])): ", res.append(s[i] + solve(s[:i] + s[i+1:], b[1:])))
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			#print("res: ", res)
			#print("s: ", s)
			#print("b: ", b)
			#print("")
			res.append(s[i] + solve(s[:i] + s[i+1:], b[1:]))
			#print("res: ", res)
			#print("s: ", s)
			#print("b: ", b)
			#print("")
		b[0] += (len(s) - i)
		b[i] += i
	#print("res: ", res)
	#print("s: ", s)
	#print("b: ", b)
	#print("")
	if len(res) > 0:
		return min(res)
	return ""

q = int(input())
for i in range(q):
	s = input()
	m = int(input())
	b = [int(x) for x in input().split()]
	print(solve(s, b))