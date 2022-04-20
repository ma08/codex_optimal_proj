

def main():
    n = int(input())
    a = list(map(int, input().split()))
    disturbed = [i for i in range(1, n - 1) if a[i - 1] == a[i + 1] == 1 and a[i] == 0]
    if len(disturbed) == 0:
        print(0)
    else:
        min_disturbed = min(disturbed)
        max_disturbed = max(disturbed)
        left_disturbed = [i for i in range(1, min_disturbed) if a[i - 1] == a[i + 1] == 1 and a[i] == 0]
        right_disturbed = [i for i in range(max_disturbed + 1, n - 1) if a[i - 1] == a[i + 1] == 1 and a[i] == 0]
        if len(left_disturbed) == 0:
            print(1)
        elif len(right_disturbed) == 0:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()