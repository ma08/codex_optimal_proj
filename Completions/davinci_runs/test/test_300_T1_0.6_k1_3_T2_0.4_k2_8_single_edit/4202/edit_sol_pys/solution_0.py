import math


def main():
    a, b = map(int, input().split())

    if a == 1:
        print(0) 
        return

    ans = float('inf')

    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            ans = min(ans, i)
            ans = min(ans, a//i)

    for i in range(2, int(math.sqrt(b))+1):
        if b % i == 0:
            ans = min(ans, i)
            ans = min(ans, b//i)

    if ans == float('inf'):
        print(b-a)
    else:
        print(ans)


if __name__ == "__main__":
    main()
