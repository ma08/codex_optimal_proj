import os
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 8)

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# sys.setrecursionlimit(10 ** 6)



H, W = map(int, input().split())

for i in range(H):
    print('#' + input() + '#', flush=True)
print('#' * (W + 2), flush=True)
