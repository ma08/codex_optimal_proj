

def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	cnt = [0 for _ in range(1000001)]
	for i in range(n):
		cnt[a[i]] += 1
	ans = 0
	for i in range(1000001):
		ans += cnt[i] // 2
	print(ans)

if __name__ == '__main__':
	main()
