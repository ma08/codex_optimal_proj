

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1: #1つしかない場合はそれを出力
        print(a[0])
        return
    if n == 2: #2つしかない場合は大きい方を出力
        print(max(a))
        return
    if n % 2 == 0:
        print(sum(a) - max(a))
        return
    print(sum(a) - min(a))

if __name__ == "__main__":
    main()
