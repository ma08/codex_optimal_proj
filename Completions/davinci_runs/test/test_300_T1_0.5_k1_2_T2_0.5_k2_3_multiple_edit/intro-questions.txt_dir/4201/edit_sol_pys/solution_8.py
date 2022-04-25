

def count_patterns(H, W, K):
	ans = 0
	for i in range(2 ** H):
		h = bin(i)[2:].zfill(H)
		for j in range(2 ** W):
			w = bin(j)[2:].zfill(W)
			if h.count('1') + w.count('1') == K:
				ans += 1
		return ans

H, W, K = map(int, input().split())

print(count_patterns(H, W, K))
