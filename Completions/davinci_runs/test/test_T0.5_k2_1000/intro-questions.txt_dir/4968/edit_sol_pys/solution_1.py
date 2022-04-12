

def main():
    n, s, r = map(int, input().split())  # n is number of seats, s is number of damaged seats, r is number of reserved seats
    damaged = set(map(int, input().split()))
    reserved = set(map(int, input().split()))
    count = 0
    for i in range(1, n+1):
        if i in damaged:
            if i-1 in reserved and i+1 in reserved:
                reserved.remove(i-1)
                reserved.remove(i+1)
            elif i-1 in reserved:
                reserved.remove(i-1)
            elif i+1 in reserved:
                reserved.remove(i+1)
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
