

def main():
    """
    The main function contains the main logic of the program.
    """
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[(i + j) // 2] == m:
                count += 1
    print(count)


if __name__ == "__main__":
    main()