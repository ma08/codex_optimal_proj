

def paint_red(h, w, k):
	ans = 0
	for i in range(2 ** h):
		h_str = bin(i)[2:].zfill(h)
		for j in range(2 ** w):
			w_str = bin(j)[2:].zfill(w)
			if h_str.count('1') + w_str.count('1') == k:
				ans += 1
	return ans

H, W, K = map(int, input().split())

print(paint_red(H, W, K))
