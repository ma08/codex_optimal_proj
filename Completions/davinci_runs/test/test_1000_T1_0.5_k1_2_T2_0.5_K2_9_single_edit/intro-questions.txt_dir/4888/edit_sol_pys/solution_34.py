

def main():
    # Get input
    n, t = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    # Iterate through tasks and see if they can be completed
    total = 0
    for i in range(n):
        total += times[i]
        if total > t:
            print(i)
            break
    else:
        print(n)

if __name__ == '__main__':
    main()
