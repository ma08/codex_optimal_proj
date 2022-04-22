

def main():
    x = int(input())
    print(x//500*1000 + x%500//5*5)  # 問題文を読み間違えていたため、5円玉の計算も足していた。

if __name__ == '__main__':
    main()
