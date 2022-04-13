import sys

def main():
    n, a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    e = [int(x) for x in sys.stdin.readline().rstrip().split()]

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
