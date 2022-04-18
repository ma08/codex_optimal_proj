
def main():
    f_in = open("file.in", 'r')
    n = int(f_in.readline())  # number of test cases
    for i in range(n):
        n = int(f_in.readline())
        print(count_reachable(n))


def count_reachable(n):
    if n == 1:  # base case
        return 2
    return count_reachable(n-1) + is_reachable(n-1, n)  # recursive call

def is_reachable(n, m):
    if n == m:  # base case
        return 1
    if n < 1:  # base case
        return 0
    if n % 10 == 0:  # recursive call
        return is_reachable(n//10, m)
    return is_reachable(n-1, m)  # recursive call

if __name__ == "__main__":
    main()
