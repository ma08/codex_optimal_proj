

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    for i in range(1, n):
        if a[i] * a[i - 1] < 0:
            res += 1
    print(res)

if __name__ == '__main__':
    main()