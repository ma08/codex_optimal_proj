
import sys

def main():
    line = sys.stdin.readline().rstrip('\r\n')  # 改行コードを削除
    a, b = map(int, line.split())  # 文字列を空白で区切ってリストに

    for i in range(1, 100):
        if int(i * 1.08) == a and int(i * 1.1) == b:
            print(i)
            sys.exit()
    print(-1)

if __name__ == '__main__':
    main()
