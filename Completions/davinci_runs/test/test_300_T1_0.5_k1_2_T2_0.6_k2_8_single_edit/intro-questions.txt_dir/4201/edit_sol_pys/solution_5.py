

def paint_red(H, W, K):
	ans = 0
	for i in range(2 ** (H - 1)):
		h = bin(i)[2:]
		for j in range(2 ** (W - 1)):
			w = bin(j)[2:]
			if h.count('1') + w.count('1') == K:
				ans += 1
	return ans

H, W, K = map(int, input().split())

print(paint_red(H, W, K))
