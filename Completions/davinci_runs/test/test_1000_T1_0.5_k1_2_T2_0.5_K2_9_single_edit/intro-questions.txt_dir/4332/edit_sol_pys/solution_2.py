

def main():
    n = int(input())
    digits = [int(i) for i in str(n)]  # ここでdigitsに1桁ずつの数字を格納
    if n % sum(digits) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
