

def main():
    # read input and split it into a list
    n, m = input().split()
    n = int(n)
    m = int(m)

    # read the list of integers
    integers = input().split()
    integers = [int(x) for x in integers]

    # create a list of the sums
    sums = []
    for i in range(n):
        for j in range(i + 1, n):
            sums.append(integers[i] + integers[j])

    # find the number of sums that are divisible by m
    count = 0
    for s in sums:
        if s % m == 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
