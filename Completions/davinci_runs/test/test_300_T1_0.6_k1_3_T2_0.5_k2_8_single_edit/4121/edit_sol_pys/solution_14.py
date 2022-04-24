

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_h = max(a)
    min_h = min(a)
    if max_h - min_h > 1: print('NO')
    else:
        print('YES') 


if __name__ == "__main__":
    main()
