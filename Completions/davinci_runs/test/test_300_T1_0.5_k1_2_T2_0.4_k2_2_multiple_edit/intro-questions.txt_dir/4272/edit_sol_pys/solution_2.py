import sys
sys.setrecursionlimit(10 ** 6)

def main():
    n = int(input())
    s = input()

    count = 0

    for i in range(n - 2):
        if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
            count += 1

    print(count)

if __name__ == '__main__':
    main()
