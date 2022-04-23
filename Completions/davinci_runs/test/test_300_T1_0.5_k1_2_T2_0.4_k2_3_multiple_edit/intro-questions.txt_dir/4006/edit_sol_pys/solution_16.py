

def main():
    with open("input.txt", "r") as f_in:
        n = int(f_in.readline())
        with open("output.txt", "w") as f_out:
            print(count_reachable(n), file=f_out)

def count_reachable(n):
    if n == 1:
        return 2
    return count_reachable(n-1) + is_reachable(n-1, n)

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
