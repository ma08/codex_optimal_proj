

def main():
    a, b, c = [int(x) for x in input().split()]  # 整数の入力
    if a + b >= c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
