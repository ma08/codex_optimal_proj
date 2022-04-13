
import sys

def main():
    n = int(sys.stdin.readline().rstrip()) # rstrip()は文字列の末尾の改行コードを削除する
    a = list(map(int, sys.stdin.readline().rstrip().split())) # split()は文字列を空白文字で区切ってリストにする
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()
