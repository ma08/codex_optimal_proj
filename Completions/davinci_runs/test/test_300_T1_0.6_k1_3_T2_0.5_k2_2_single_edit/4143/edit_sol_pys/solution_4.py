

def main():
    n = int(input())  # 時間
    a = int(input())  # 入力
    b = int(input())  # 入力
    c = int(input())  # 入力
    d = int(input())  # 入力
    e = int(input())  # 入力

    l = [a, b, c, d, e]  # 入力をリストに格納
    l.sort()  # 昇順に並び替え

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
