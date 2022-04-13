H, W = map(int, input().split())

for i in range(H):
    print('#' + input() + '#', flush=True)

print('#' * (W + 2), flush=True)
