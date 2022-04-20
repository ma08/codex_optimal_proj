
def main():
    a, b = map(int, input().split())  # a: 支払う金額, b: 持っている金額
    count = 0
    while b > 0:  # 持っている金額が0より大きい間繰り返す
        if b >= a:
            b -= a
        else:
            b -= 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()
