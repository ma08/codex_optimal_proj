import sys

def main():
    h, w = map(int, sys.stdin.readline().split())  # 入力
    matrix = [sys.stdin.readline() for _ in range(h)]
    for i in range(2 * h):
        print(matrix[i // 2])

if __name__ == '__main__':
    main()
