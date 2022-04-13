
print('#' * (W + 2))
H, W = map(int, input().split())  # 入力

for i in range(H):  # 出力
    print('#' + input().rstrip() + '#')

print('#' * (W + 2))
