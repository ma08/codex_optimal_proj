# https://open.kattis.com/problems/r2

def main():
    r1, s = list(map(int, input().split()))
    print(s * 2 - r1)

if __name__ == '__main__':
    main()
