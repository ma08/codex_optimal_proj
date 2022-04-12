import sys

def main():
    n = int(input())
    times = [int(x) for x in input().split()]
    times.sort(reverse=True)

    a = 0
    b = 0
    for i in range(n):
        if i % 2 == 0:
            a += times[i]
        else:
            b += times[i]

    print(max(a, b), min(a, b))

if __name__ == '__main__':
    main()
