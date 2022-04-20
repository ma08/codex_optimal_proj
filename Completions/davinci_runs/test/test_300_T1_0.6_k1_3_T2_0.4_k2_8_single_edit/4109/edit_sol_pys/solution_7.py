

import sys, collections
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 20min

def main():
    N = int(readline())
    S = [readline().rstrip() for _ in range(N)]
    T = [readline().rstrip() for _ in range(N)]

    C = collections.Counter(S)
    D = collections.Counter(T)

    if C == D:
        print("Yes")
    print("No")

if __name__ == "__main__":
    main()
