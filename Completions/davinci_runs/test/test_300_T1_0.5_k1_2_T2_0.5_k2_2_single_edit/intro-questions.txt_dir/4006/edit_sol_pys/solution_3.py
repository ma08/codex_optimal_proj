

# def main():
#     f_in = open("f.in", "r")
#     n = int(f_in.readline())
#     print(count_reachable(n))

def count_reachable(n):
    if n == 0:
        return 1
    return count_reachable(n-1) + is_reachable(n-1, n-1)

def is_reachable(n, m):
    if n == m:
        return 2
    if n < 1:
        return 0
    if n % 10 == 0:
        return is_reachable(n//10, m)
    return is_reachable(n-1, m)

if __name__ == "__main__":
    print(count_reachable(10))
