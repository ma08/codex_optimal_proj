

def paint_red(h, w, k):
	ans = 0
	for i in range(2 ** h):
		hh = bin(i)[2:].zfill(h)
		for j in range(2 ** w):
			ww = bin(j)[2:].zfill(w)
			if hh.count('1') + ww.count('1') == k:
				ans += 1
	return ans

h, w, k = map(int, input().split())

print(paint_red(h, w, k))
