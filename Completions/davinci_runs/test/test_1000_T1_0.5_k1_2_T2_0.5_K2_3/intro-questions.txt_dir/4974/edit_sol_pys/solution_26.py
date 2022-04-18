


def main():
    r, n = map(int, input().split())
    booked = set()
    for _ in range(n):
        booked.add(int(input()))
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == '__main__':
    main()
