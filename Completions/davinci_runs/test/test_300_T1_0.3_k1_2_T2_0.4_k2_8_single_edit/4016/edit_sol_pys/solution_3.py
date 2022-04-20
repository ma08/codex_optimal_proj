
import sys

def main():
    n = int(sys.stdin.readline())
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                ans[i * j] += 1
    print(ans.count(8))

if __name__ == "__main__":
    main()
