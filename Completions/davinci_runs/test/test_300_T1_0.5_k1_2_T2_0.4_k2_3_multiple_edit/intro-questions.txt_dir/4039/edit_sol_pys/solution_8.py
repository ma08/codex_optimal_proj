
import sys

def main():
    n = int(input())
    s = input()
    t = input()

    ans = []
    for i in range(n):
        ans.append(s[i])
        ans.append(t[i])

    print("".join(ans))

if __name__ == '__main__':
    main()
