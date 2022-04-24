

def main():
    x, n = map(int, input().split())  # x:入力した数字, n:入力された数字の数
    p = sorted(list(map(int, input().split())))  # p:入力された数字のリスト

    if x < p[0]:
        print(x - p[0])
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(p[i+1] - x, x - p[i]))
                break

if __name__ == '__main__':
    main()
