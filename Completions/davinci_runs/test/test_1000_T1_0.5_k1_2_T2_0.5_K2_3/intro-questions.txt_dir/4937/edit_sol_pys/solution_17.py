import sys

def main():
    n, a = map(int, input().split())
    e = map(int, input().split())

    e.sort()
    count = 0
    for i in range(n):
        if a < e[i]:
            break
        a -= e[i]
        count += 1

    print(count)

if __name__ == "__main__":
    main()
