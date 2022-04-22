

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split())  # split()によって、スペース区切りで入力された文字列をint型に変換し、map()で返り値のmapオブジェクトをiterablesに変換する
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
