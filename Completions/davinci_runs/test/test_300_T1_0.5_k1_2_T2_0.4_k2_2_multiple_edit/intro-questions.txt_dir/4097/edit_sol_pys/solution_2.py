

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        d = [a[i] - a[i - 1] for i in range(1, n)]  # 求出每个相邻数字的差
        d.sort()
        if d[0] == d[-1]:
            print(0)
        else:
            print(2)

if __name__ == '__main__':
    main()
