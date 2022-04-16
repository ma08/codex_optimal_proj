

def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	cnt = {}
	for i in a:
		if i in cnt:
			cnt[i] += 1
		else:
			cnt[i] = 1
	ans = 0
	for i in topics:
		ans += cnt[i] - cnt[i] % 2
	print(ans)

if __name__ == '__main__':
	main()
