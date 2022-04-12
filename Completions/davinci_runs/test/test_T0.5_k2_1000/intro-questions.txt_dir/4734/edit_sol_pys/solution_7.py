

def main():
    X, Y = input().split()  # X: 語尾, Y: 語頭
    if X[-1] == 'e':
        print(X + 'x' + Y)
    elif X[-1] in 'aiou':  # 語尾が母音の場合
        print(X[:-1] + 'ex' + Y)
    elif X[-2:] == 'ex':  # 語尾がexの場合
        print(X + Y)
    else:
        print(X + 'ex' + Y)

main()
