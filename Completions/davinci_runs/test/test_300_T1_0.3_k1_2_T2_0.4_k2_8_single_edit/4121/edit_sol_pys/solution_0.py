# https://codeforces.com/problemset/problem/1360/A

def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a * 2 <= b:
            print(a * a)
        else:
            print((a + b) * (a + b) // 4)

if __name__ == "__main__":
    main()
