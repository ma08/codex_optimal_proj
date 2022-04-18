# https://codeforces.com/problemset/problem/734/A


def main():
    input()
    s = input()
    a = 0
    d = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += 1    
        elif s[i] == 'D':
            d += 1

    if a > d:
        print("Anton")
    elif d > a:
        print("Danik")
    elif a == d:
        print("Friendship")


if __name__ == '__main__':
    main()
