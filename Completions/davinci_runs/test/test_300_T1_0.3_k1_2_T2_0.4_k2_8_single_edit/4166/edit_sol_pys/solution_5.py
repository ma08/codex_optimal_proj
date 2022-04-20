import sys
input = sys.stdin.readline


N, M = map(int, input().split())  # N: 桁数 M: 制約の数
# 制約の数だけsとcを取得

s = []
c = []
for _ in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)
# 制約を満たす数を探す

ans = -1
for i in range(10**N):
    i_str = str(i)  # iを文字列に変換
    if len(i_str) != N:  # 桁数がNでない場合はスキップ
        continue
        # 制約を満たさない場合は次の数を試す
    for j in range(M):
        if i_str[s[j]-1] != str(c[j]):
            break
    else:
        ans = i
        break

print(ans)
