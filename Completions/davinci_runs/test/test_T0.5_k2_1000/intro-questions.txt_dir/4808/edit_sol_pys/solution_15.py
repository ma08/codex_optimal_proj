

def main():
    n, d_m = map(int, input().split())  # n is the number of years and d_m is the day of the month
    d_n = list(map(int, input().split()))  # d_n is the list of days of the month
    d_n.append(d_m)  # add the day of the month to the list
    count = 0
    for i in range(n-1, -1, -1):  # iterate through the list backwards
        if d_n[i] > d_n[i+1]:  # if the current day is greater than the next day
            count += 1
        else:
            break
    print("It hadn't snowed this early in " + str(count) + " years.")

if __name__ == "__main__":
    main()
