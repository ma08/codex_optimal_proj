

def main():
    f_in = open("f.in", "r")  # open file
    n = int(f_in.readline())  # read first line
    print(count_reachable(n))  # print result

# count number of reachable numbers

def count_reachable(n):
    if n == 1:
        return 2
    return count_reachable(n - 1) + is_reachable(n - 1, n)

# check if n is reachable from m

def is_reachable(n, m):
    if n == m:
        return 1
    if n < 1:
        return 0
    if n % 10 == 0:
        return is_reachable(n // 10, m)
    return is_reachable(n - 1, m)


if __name__ == "__main__":
    main()
