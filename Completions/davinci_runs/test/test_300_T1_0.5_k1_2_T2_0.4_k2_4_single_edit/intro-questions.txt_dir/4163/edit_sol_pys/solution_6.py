

def main():
    n = int(input()) # 入力
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split()) # 入力
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes") # 出力
            break
    else:
        print("No") # 出力

if __name__ == '__main__':
    main()
