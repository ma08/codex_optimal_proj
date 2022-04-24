
n = int(input())

ans = 0
for i in range(1, n + 1):
    num = len(str(i))  # 桁数を数える
    if num % 2 != 0:
        ans += 1

print(ans)
