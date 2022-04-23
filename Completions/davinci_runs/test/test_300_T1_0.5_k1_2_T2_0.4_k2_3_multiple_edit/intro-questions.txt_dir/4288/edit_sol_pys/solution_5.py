

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or a == c:  # a, b, cのいずれかが等しい場合はYesを出力
        print("Yes")
    else:
        print("No")  # a, b, cが全て等しくない場合はNoを出力する

if __name__ == '__main__':
    main()
