
def main():
    N = int(input())
    cnt = 0
    for i in range(N):
        d1, d2 = map(int, input().split()) # 入力を2つに分割
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            break
    else: # for文がbreakされなかった場合に実行
        print("No")

if __name__ == '__main__':
    main()
