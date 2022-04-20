
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    max_h = max(arr)
    min_h = min(arr)
    if max_h - min_h > 1: print('NO')
    else:
        print('YES') 


if __name__ == "__main__":
    main()
