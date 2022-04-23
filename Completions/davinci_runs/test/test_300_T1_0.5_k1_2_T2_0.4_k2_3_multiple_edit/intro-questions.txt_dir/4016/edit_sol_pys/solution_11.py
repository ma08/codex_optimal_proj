
def main():
    n, k = map(int, input().split())
    t = input()
    print(t*(k//n) + t[:k%n])  # 文字列の足し算は繰り返し

if __name__ == "__main__":
    main()
