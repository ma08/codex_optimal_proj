
def main():
	N = int(input())
	count = 0
	for i in range(N):
		d1, d2 = map(int, input().split()) # 右辺はタプルになる
		if d1 == d2: # 同じ値ならカウントをインクリメント
			count += 1
		else:
			count = 0
		if count >= 3:
			break
	print("Yes" if count >= 3 else "No")

if __name__ == "__main__":
	main()
