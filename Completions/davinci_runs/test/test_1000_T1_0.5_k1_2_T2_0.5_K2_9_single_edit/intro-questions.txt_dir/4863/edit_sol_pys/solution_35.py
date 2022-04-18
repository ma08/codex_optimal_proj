

n = int(input())
ans = input().split()

ans = [ans[i] for i in range(len(ans)) if i != n-1] # リスト内包表記でn-1番目以外を取り出す
# 取り出したリストの要素数を出力

print(len(ans))
