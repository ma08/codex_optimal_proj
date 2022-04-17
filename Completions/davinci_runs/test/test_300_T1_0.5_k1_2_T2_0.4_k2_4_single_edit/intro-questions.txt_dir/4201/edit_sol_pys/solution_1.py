

def paint_red(h, w, k):
	ans = 0
	for i in range(2 ** h):
		h_ = bin(i)[2:].zfill(h)
		for j in range(2 ** w):
			w_ = bin(j)[2:].zfill(w)
			if h_.count('1') + w_.count('1') == k:
				ans += 1
	return ans

h, w, k = map(int, input().split())

print(paint_red(h, w, k))
