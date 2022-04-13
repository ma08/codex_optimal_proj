

def main():
    r, n = map(int, input().split())  # type: int, int
    booked = set()
    for _ in range(n):
        booked.add(int(input()))  # type: int
    for i in range(1, r+1):
        if i not in booked:
            print(i)  # type: int
            return
    print("too late")

if __name__ == '__main__':
    main()
