
import sys

def main():
    d, t, s = map(int, sys.stdin.readline().split())
    if d / s <= t: # 小数点以下切り捨て
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
