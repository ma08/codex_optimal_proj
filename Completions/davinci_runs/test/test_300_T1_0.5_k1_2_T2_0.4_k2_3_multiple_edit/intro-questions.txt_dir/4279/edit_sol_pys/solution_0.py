

def main():
    n, m = map(int, input().split())
    print(find(n, m))

def find(n, m):
    if m == 1:
        return n
    if m == 2:
        return n - 1
    if m == 3:
        return n - 2
    
    if m > n:
        return find(n, n)
    
    return find(n - 1, m) + find(n - 1, m - 1)

if __name__ == '__main__':
    main()
