
import math

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt = 0
    if a[-1] < b[0]:
        cnt += math.ceil(n / m)
        a = b
    while len(a) > 0:
        print(a, b)
        if a[-1] < b[0]:
            cnt += math.ceil(len(a) / m)
            a = b
        else:
            for i in range(len(b)):
                if b[i] > a[-1]:
                    a = a + b[:i]
                    break
            b = b[i:]
    print(cnt)


if __name__ == "__main__":
    main()
