n = int(input())
ans = input().split()

# 一番後ろの要素を削除
ans = [ans[i] for i in range(len(ans)) if i != n-1]

print(len(ans))
