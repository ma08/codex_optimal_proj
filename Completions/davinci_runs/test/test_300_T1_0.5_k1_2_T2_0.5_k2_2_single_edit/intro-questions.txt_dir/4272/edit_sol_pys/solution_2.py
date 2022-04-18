import sys
input = sys.stdin.readline



def main():
    N = int(input())
    S = input().rstrip()

    print(S.count("ABC"))


if __name__ == '__main__':
    main()
