
import sys
input = sys.stdin.readline

def main():
    n = int(input())  # 数列の長さ
    a = list(map(int, input().split()))  # 数列
    q = int(input())  # クエリの個数
    for i in range(q):
        b, e, k = map(int, input().split())
        print(sum(a[b - 1:e]) // k)

if __name__ == "__main__":
    main()
