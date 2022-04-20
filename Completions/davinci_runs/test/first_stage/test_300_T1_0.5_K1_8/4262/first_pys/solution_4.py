

def main():
	n = int(input())
	p = list(map(int, input().split()))
	q = list(map(int, input().split()))
	count = 0
	for i in range(n):
		if p[i] != q[i]:
			count += 1
	print(count-1)

if __name__ == '__main__':
	main()