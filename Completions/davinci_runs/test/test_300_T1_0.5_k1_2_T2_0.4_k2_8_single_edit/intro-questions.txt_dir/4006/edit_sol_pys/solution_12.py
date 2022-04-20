

def main():
    f_in = open("f.in", "r")  # open file
    n = int(f_in.readline())
    print(count_reachable(n))  # print result


def count_reachable(n):  # count reachable numbers
    if n == 1:
        return 2
    return count_reachable(n-1) + is_reachable(n-1, n)  # recursive call


def is_reachable(n, m):  # check if n is reachable from m
    if n == m:
        return 1
    if n < 1:
        return 0
    if n % 10 == 0:
        return is_reachable(n//10, m)  # recursive call
    return is_reachable(n-1, m)  # recursive call


if __name__ == "__main__":
    main()
