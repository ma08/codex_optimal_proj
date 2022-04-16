

def main():
    r, n = map(int, input().split())  # read number of rooms and number of bookings
    booked = set()  # set of booked rooms
    for _ in range(n):
        booked.add(int(input()))  # read each booking
    for i in range(1, r+1):
        if i not in booked:  # check if room is not booked
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
