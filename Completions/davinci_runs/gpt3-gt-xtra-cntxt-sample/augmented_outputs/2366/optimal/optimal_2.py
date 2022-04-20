import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        stack = []
        bad = 0
        for i in range(n):
            while stack and stack[-1]>a[i]:
                stack.pop()
                bad += 1
            stack.append(a[i])
        print(bad)

if __name__ == "__main__":
    main()