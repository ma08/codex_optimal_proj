

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    max_val = max(arr)
    min_val = min(arr)
    if arr.count(max_val) == 1:
        print(max_val - min_val)
    else:
        arr.remove(max_val)
        print(max(arr) - min(arr))


if __name__ == "__main__":
    main()