

def main():
    r, n = map(int, input().split())  # r is the number of rooms and n is the number of booked rooms
    booked = set()
    for _ in range(n):
        booked.add(int(input()))  # add all the booked rooms to the set
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
