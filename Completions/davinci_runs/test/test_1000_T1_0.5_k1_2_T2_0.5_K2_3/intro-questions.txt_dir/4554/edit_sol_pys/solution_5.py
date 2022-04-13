import sys

def main():
    w, a, b = map(int, input().split())
    print(max(0, b - (a + w) + 1)) # 右に行くときと左に行くときの大きい方を出力

if __name__ == "__main__":
    main()
