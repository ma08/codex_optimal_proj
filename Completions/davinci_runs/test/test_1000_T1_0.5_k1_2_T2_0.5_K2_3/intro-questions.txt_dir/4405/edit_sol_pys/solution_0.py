

def main():
	n = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	topics = set()
	for i in a:
		topics.add(i)
	topics = list(topics)
	topics.sort()
	cnt = {}
	for i in topics:
		cnt[i] = 0
	for i in a:
		cnt[i] += 1
	#print(topics)
	#print(cnt)
	ans = 0
	for i in topics:
		ans += cnt[i] - cnt[i] // 2
	print(ans)

if __name__ == '__main__':
	main()
