

def main():
    x, n = map(int, input().split())  # x:最終的に求めたい数字, n:ピタゴラス数の要素数
    p = sorted(list(map(int, input().split())))  # p:ピタゴラス数

    if x < p[0]:
        print(p[0] - x)
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))
                break

if __name__ == '__main__':
    main()
