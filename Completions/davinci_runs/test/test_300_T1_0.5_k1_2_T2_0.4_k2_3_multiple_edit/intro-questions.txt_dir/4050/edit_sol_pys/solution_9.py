

def find_blocks(a, n):
    s = sum(a)
    if s % n != 0:
        return -1
    s //= n
    l = 0
    r = 0
    cur = 0
    res = 0
    while r < n:
        if cur < s:
            cur += a[r]
            r += 1
        else:
            cur -= a[l]
            l += 1
        if cur == s:
            res += 1
    return res

def main():
    n = int(input("Enter the number of elements: "))
    a = [int(s) for s in input("Enter the elements: ").split()]
    print(find_blocks(a, n))

if __name__ == "__main__":
    main()
