

def main():
    n = int(input())
    array = list(map(int, input().split()))
    max_diff = 0
    for i in range(n-1):
        diff = abs(array[i] - array[i+1])
        if diff > max_diff:
            max_diff = diff
    print(max_diff)


if __name__ == '__main__':
    main()
