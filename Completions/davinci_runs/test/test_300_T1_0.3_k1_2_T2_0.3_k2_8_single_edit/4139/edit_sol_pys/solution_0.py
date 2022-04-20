

def main():
    n = int(input())  # 入力
    count = 0
    for i in range(1, n+1):  # 1からnまでの数字を調べる
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
