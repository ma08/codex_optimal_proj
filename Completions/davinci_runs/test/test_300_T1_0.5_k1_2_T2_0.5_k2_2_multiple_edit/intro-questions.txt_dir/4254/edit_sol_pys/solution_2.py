
import sys

def main():
    sheeps, wolves = map(int, sys.stdin.readline().split())  # split() 공백 기준으로 나눠서 리스트로 반환

    if sheeps < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
