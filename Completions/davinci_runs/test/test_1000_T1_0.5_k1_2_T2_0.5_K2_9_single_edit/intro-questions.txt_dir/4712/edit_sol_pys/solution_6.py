H, W = map(int, input().split())
area = []


for i in range(H):
    area.append('#' + input() + '#')

for i in range(H):
    print('#' + input() + '#')

print('#' * (W + 2))
