
import sys

def main():
	n = int(sys.stdin.readline())
	seq = list(map(int, sys.stdin.readline().split()))
	if n <= 2:
		print(0)
		return
	d = seq[1] - seq[0]
	for i in range(2, n):
		if seq[i] - seq[i-1] != d:
			if seq[i-1] - seq[i-2] == d:
				if seq[i] - seq[i-1] == d - 1:
					seq[i] += 1
					print(1)
					return
				elif seq[i] - seq[i-1] == d + 1:
					seq[i] -= 1
					print(1)
					return
				else:
					print(-1)
					return
			elif seq[i-1] - seq[i-2] == d - 1:
				if seq[i] - seq[i-1] == d:
					seq[i-1] += 1
					print(1)
					return
				elif seq[i] - seq[i-1] == d - 1:
					seq[i] += 1
					seq[i-1] += 1
					print(2)
					return
				else:
					print(-1)
					return
			elif seq[i-1] - seq[i-2] == d + 1:
				if seq[i] - seq[i-1] == d:
					seq[i-1] -= 1
					print(1)
					return
				elif seq[i] - seq[i-1] == d + 1:
					seq[i] -= 1
					seq[i-1] -= 1
					print(2)
					return
				else:
					print(-1)
					return
			else:
				print(-1)
				return
	print(0)

if __name__ == '__main__':
	main()