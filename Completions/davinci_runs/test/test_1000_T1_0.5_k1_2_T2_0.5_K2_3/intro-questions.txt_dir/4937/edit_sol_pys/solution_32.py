import sys

def main():
    values1 = list(map(int, sys.stdin.readline().strip().split()))
    n = values1[0]
    a = values1[1]
    values2 = list(map(int, sys.stdin.readline().strip().split()))
    e = sorted(values2, reverse=True)
    result = 0
    for i in range(n):
        if a > e[i]:
            a -= e[i]
            result += 1
        else:
            break
    print(result)

if __name__ == "__main__":
    main()
