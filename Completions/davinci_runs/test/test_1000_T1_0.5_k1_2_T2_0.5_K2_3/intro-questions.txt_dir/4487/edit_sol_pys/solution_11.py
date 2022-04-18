
def main():
    a, b, c = input().split()  # a,b,cを空白で区切って3つの変数に格納
    if a[-1] == b[0] and b[-1] == c[0]:
        print("YES")  # aの最後とbの最初が一致して、bの最後とcの最初が一致していたらYES
    else:
        print("NO")  # それ以外はNO

if __name__ == '__main__':
    main()  # main関数を呼び出す
