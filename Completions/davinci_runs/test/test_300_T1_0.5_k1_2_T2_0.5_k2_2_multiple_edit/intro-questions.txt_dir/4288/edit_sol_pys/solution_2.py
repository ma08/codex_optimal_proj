

def main():
    a, b, c = map(int, input().split())  # map(int, input().split())は、入力を空白で区切って、int型に変換して、リストに入れる
    if a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
