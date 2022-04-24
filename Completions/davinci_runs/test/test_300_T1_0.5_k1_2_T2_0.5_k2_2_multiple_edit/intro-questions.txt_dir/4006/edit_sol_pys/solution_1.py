
def main():
    f_in = open("f.in", "r")  # open the file with name 'f.in'
    n = int(f_in.readline())
    print(count_reachable(n))  # print the answer

# count the number of reachable numbers

def count_reachable(n):
    if n == 1:
        return 2
    return count_reachable(n - 1) + is_reachable(n - 1, n)

# check if the number is reachable

def is_reachable(n, m):
    if n == m:
        return 1
    if n < 1:
        return 0
    if n % 10 == 0:  # if last digit is 0, we can divide by 10
        return is_reachable(n // 10, m)
    return is_reachable(n - 1, m)


if __name__ == "__main__":
    main()
