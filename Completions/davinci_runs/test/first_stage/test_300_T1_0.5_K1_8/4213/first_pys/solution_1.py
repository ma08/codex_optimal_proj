

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_val = min(a)
    max_val = max(a)
    print(max(max_val-min_val, max_val-a[a.index(min_val)-1], a[a.index(max_val)-1]-min_val))

if __name__ == '__main__':
    main()