"""
https://codeforces.com/problemset/problem/1352/A
"""



def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        if n == 1:
            print(0)
        else:
            print(m * 2 - n)


if __name__ == "__main__":
    main()
