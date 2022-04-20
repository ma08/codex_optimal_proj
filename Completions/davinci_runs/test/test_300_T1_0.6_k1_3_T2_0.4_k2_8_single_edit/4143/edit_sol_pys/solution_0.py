

def main():
    n = int(input())  # 所持金
    a = int(input())  # 一人当たりの金額
    b = int(input())  # 一人当たりの金額
    c = int(input())  # 一人当たりの金額
    d = int(input())  # 一人当たりの金額
    e = int(input())  # 一人当たりの金額

    l = [a, b, c, d, e]
    l.sort()  # 小さい順に並び替え

    if n <= l[0]:  # 一人当たりの金額の最小値が所持金より大きい場合
        print(1)
    else:  # 一人当たりの金額の最小値が所持金より小さい場合
        print(2)  # 2人で買う

if __name__ == '__main__':
    main()
