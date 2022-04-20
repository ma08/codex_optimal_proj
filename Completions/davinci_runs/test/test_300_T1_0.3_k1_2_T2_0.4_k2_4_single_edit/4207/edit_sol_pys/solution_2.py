import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c = sorted(c)
    cnt = 0
    for i in range(n):
        if c[i] == 0:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
