import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = -1
    for i in range(n - 1):
        if a[i] >= b[i]:
            i += 1
            continue
        elif a[i] < b[i] and a[i + 1] >= b[i] - a[i]:
            a[i + 1] -= b[i] - a[i]
        elif a[i] < b[i] and a[i + 1] < b[i] - a[i]:
            ans = i + 1
            break
    print(ans + 1)

if __name__ == '__main__':
    main()
