
import sys

def main():
    d, t, s = map(int, sys.stdin.readline().split())
    if d / s <= t:  # 到達時間が時間内に収まるか
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
