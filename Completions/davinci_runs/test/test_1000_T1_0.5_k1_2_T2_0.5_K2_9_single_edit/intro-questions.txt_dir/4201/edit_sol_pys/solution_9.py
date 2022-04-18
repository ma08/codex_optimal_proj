
def paint_red(h, w, k):
	ans = 0
	for i in range(2 ** h):
		H = bin(i)[2:].zfill(h)
		for j in range(2 ** w):
			W = bin(j)[2:].zfill(w)
			if H.count('1') + W.count('1') == k:
				ans += 1
	return ans
H, W, K = map(int, input().split())

print(paint_red(H, W, K))
