

	'''
	H: 高さ
	W: 幅
	K: 赤マスの数
	'''
def paint_red(H, W, K):
	ans = 0
	for i in range(2 ** H):
		h = bin(i)[2:].zfill(H) # 2進数に変換し、0で埋める
		for j in range(2 ** W):
			w = bin(j)[2:].zfill(W) # 2進数に変換し、0で埋める
			if h.count('1') + w.count('1') == K: # 赤マスの数がKであるかどうか判定
				ans += 1
	return ans

H, W, K = map(int, input().split())

print(paint_red(H, W, K))
