

def main():
    f_in = open("f.in", "r", encoding='utf-8')
    n = int(f_in.readline()) + 1
    print(count_reachable(n))

def count_reachable(n, m=None):
    if m is None:
        m = n
    if n == 1:
        return 2
    return count_reachable(n-1, m) + is_reachable(n-1, m)

def is_reachable(n, m):
    if n < 1:
    if n == m:
        return 1
        return 0
    if n % 10 == 0:
        return is_reachable(n//10, m)
    return is_reachable(n-1, m)

if __name__ == "__main__":
    main()
