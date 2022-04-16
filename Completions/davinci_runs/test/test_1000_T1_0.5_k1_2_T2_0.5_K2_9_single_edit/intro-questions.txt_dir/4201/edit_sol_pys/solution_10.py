

def paint_red(h, w, k):
	ans = 0
	for i in range(2 ** h):
		h_bin = bin(i)[2:].zfill(h)
		for j in range(2 ** w):
			w_bin = bin(j)[2:].zfill(w)
			if h_bin.count('1') + w_bin.count('1') == k:
				ans += 1
	return ans

h, w, k = map(int, input().split())

print(paint_red(h, w, k))
