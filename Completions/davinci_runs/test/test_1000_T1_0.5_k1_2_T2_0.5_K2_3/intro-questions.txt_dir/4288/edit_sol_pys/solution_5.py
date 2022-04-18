

def main():
    a, b, c = map(str, input().split())  # 入力された文字列をsplitで分割してリストにする
    if a[-1] == b[0] and b[-1] == c[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
