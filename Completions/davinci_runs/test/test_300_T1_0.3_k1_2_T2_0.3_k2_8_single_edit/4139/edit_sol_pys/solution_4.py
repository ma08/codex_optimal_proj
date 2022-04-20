

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):  # 1~nまでの数字を順に調べる
        if '7' in str(i) and '5' in str(i) and '3' in str(i):  # iが7,5,3を含むか調べる
            count += 1  # 含むならカウントアップ
    print(count)

if __name__ == '__main__':
    main()
