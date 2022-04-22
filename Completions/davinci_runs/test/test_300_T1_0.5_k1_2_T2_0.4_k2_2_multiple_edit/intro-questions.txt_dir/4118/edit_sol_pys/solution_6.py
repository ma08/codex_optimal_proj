
def main():
    a, b = map(int, input().split())
    if a > 10 or a < 1 or b > 10 or b < 1:  # 条件判定
        print(-1)
        return
    print(a * b)

if __name__ == '__main__':
    main()
