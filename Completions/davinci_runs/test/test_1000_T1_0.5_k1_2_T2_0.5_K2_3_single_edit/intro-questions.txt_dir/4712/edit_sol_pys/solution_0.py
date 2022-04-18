
import sys

H, W = map(int, input().split())

for i in range(H):
    print('#' + sys.stdin.readline() + '#')

print('#' * (W + 2))
