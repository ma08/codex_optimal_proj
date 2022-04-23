

def main():
    n, k = map(int, input().split())  # 整数の入力
    t = input()  # 文字列の入力
    print(t*(k//n) + t[:k%n])  # 文字列の足し算は繰り返し

if __name__ == "__main__":
    main()
