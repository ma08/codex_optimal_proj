

def main():
    n, s, r = map(int, input().split())  # n: number of seats, s: number of damaged seats, r: number of reserve seats
    damaged = set(map(int, input().split()))
    reserve = set(map(int, input().split()))
    count = 0  # count the number of people who cannot sit
    for i in range(1, n + 1):
        if i in damaged:  # if the seat is damaged
            if i-1 in reserve and i+1 in reserve:  # if the seats in the left and right are reserve seats
                reserve.remove(i-1)  # remove the seat in the left
                reserve.remove(i+1)  # remove the seat in the right
            elif i-1 in reserve:  # if the seat in the left is reserve seat
                reserve.remove(i-1)  # remove the seat in the left
            elif i+1 in reserve:  # if the seat in the right is reserve seat
                reserve.remove(i+1)  # remove the seat in the right
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
