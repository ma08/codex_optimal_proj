

# Solution

def main():
    r, n = [int(i) for i in input().split()]  # r is number of rooms, n is number of booked rooms
    booked = set()
    for i in range(n):
        booked.add(int(input()))  # add room number to set
    for i in range(1, r+1):
        if i not in booked:  # if room is not booked
            print(i)
            return
    print("too late")  # if all rooms are booked

if __name__ == "__main__":
    main()
