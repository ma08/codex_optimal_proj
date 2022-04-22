
def main():
    f_in = open("file.in", "r")
    n = int(f_in.readline())
    print(count_reachable_numbers(n))

def count_reachable_numbers(n):
    if n == 1:
        return 2
    return count_reachable_numbers(n-1) + is_reachable(n-1, n)

def is_reachable(n, m):
    if n == m:
        return 1
    if n < 1:
        return 0
    if n % 10 == 0:
        return is_reachable(n//10, m)
    return is_reachable(n-1, m)

if __name__ == "__main__":
    main()
