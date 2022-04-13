

def main():
    # Get input
    n = int(input())
    a = [int(x) for x in input().split()]

    # Get the largest number of days he can't train
    days = 0
    for i in range(n):
        if a[i] > days:
            days += 1

    print(days)

if __name__ == "__main__":
    main()
