


def count_ones(x):
	return bin(x)[2:].count('1')

def paint_black(H, W, K):
	ans = 0
	for i in range(2 ** H):
		for j in range(2 ** W):
			if count_ones(i) + count_ones(j) == K:
				ans += 1
	return ans

H, W, K = map(int, input().split())

print(paint_black(H, W, K))
