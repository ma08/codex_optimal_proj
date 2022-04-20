

def main():
    n = int(input())  # 行数

    soft = []
    hard = []

    for i in range(n):
        a, b = input().split()  # 文字列と言語
        if b == "soft":
            soft.append(a)  # ソフトウェア
        else:
            hard.append(a)

    soft.sort()
    hard.sort()

    if len(soft) > len(hard):
        print(len(hard))
    else:
        print(len(soft))

if __name__ == "__main__":
    main()
