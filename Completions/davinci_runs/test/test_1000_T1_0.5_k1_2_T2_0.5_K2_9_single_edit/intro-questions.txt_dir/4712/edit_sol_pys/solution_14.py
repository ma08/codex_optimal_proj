
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
H, W = map(int, input().split())
for i in range(H):
    print('#' + input() + '#')
print('#' * (W + 2))
