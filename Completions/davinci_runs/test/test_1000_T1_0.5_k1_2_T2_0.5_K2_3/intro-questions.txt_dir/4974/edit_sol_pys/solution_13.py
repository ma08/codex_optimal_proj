import sys

def main():
    r, n = map(int, sys.stdin.readline().split())
    booked = []
    for _ in range(n):
        booked.append(int(sys.stdin.readline()))
    booked.sort()
    for i in range(1, r + 1):
        if i not in booked:
            print(i)
            return
    print("too late")


if __name__ == '__main__':
    main()
