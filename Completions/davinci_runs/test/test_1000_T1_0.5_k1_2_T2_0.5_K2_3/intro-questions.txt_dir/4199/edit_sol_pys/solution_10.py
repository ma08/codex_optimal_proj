
import sys # sysモジュールのインポート

N, K = list(map(int,sys.stdin.readline().split()))
h = list(map(int,sys.stdin.readline().split())) # 標準入力

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1

print(count) # 標準出力
