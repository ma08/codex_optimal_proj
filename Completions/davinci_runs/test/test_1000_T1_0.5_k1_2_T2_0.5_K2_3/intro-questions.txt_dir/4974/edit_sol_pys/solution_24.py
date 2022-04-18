import sys

def main():
    r, n = map(int, sys.stdin.readline().split())
    booked = set()
    for _ in range(n):
        booked.add(int(sys.stdin.readline()))
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == '__main__':
    main()
