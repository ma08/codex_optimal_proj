

def main():
    a, b, c, d = input().split()  # 入力を受け取る
    if b == "W" and c == "E":  # 判定
        print("Yes")
    elif b == "E" and c == "W":  # 判定
        print("Yes")
    elif b == "N" and c == "S":
        print("Yes")
    elif b == "S" and c == "N":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
