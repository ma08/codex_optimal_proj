

def main():
    a, b, c = input().split()  # 入力を3つに分ける
    if b == "West" and c == "East":  # 入力した文字が条件にあったら、Yesを出力
        print("Yes")
    elif b == "East" and c == "West":
        print("Yes")
    elif b == "North" and c == "South":
        print("Yes")
    elif b == "South" and c == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
