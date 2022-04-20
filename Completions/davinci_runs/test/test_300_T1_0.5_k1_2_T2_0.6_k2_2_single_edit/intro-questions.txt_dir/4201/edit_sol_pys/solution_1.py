

def paint_red(H, W, K):
	ans = 0
	for i in range(2 ** H):
		h = bin(i)[2:].zfill(H)
		for j in range(2 ** W):
			w = bin(j)[2:].zfill(W)
			count = 0
			for k in range(H):
				for l in range(W):
					if h[k] == '1' and w[l] == '1':
						count += 1
			if count == K:
				ans += 1
	return ans

H, W, K = map(int, input().split())

print(paint_red(H, W, K))
