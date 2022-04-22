

def paint_red(H, W, K):
	ans = 0
	for i in range(2 ** H):
		h = bin(i)[2:].zfill(H)
		for j in range(2 ** W):
			w = bin(j)[2:].zfill(W)
			sum = 0
			for hh, ww in zip(h, w):
				if hh == '1' and ww == '1':
					sum += 1
			if sum == K:
				print(h)
				print(w)
				print('\n')
				ans += 1			
	return ans

H, W, K = map(int, input().split())

print(paint_red(H, W, K))
