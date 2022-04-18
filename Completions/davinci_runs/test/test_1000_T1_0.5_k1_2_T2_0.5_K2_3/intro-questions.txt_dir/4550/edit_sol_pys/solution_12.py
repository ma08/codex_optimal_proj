

def main():
    a, b, c = map(int, input().split())  # 整数の入力
    if a + b == c:  # 三辺の長さが一致しているか判定
        print("Yes")
    elif a + c == b:  # 三辺の長さが一致しているか判定
        print("Yes")
    elif b + c == a:  # 三辺の長さが一致しているか判定
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
