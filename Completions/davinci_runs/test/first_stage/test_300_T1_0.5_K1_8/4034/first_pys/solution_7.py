

import sys

def main():
	n = int(sys.stdin.readline().strip())
	s = sys.stdin.readline().strip()
	if n == 1:
		print("YES")
		print(0)
		return
	elif n == 2:
		if s[0] == s[1]:
			print("YES")
			print(0,0)
		else:
			print("YES")
			print(0,1)
		return
	else:
		print("YES")
		if s[0] == s[1]:
			print(0, end = "")
		else:
			print(1, end = "")
		for i in range(1, n - 1):
			if s[i] == s[i+1]:
				print(0, end = "")
			elif s[i] == s[i-1]:
				print(1, end = "")
			else:
				print(0, end = "")
		if s[n-2] == s[n-1]:
			print(0)
		else:
			print(1)

if __name__ == "__main__":
	main()