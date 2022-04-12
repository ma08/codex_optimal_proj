
H, W = map(int, input().split()) # H: 高さ, W: 幅

for i in range(H):
    print('#' + input() + '#')

print('#' * (W + 2))
