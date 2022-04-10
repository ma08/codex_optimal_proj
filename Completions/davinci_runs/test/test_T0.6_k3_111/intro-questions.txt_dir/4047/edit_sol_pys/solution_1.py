

def main():
    n = int(input())
    x = [int(i) for i in input().split()]

    if n == 1:
        print("0")
        return

    min_x = min(x)
    max_x = max(x)

    if max_x - min_x > 2:
        print("-1")
        return

    elif max_x - min_x == 2:
        print("1")
        return

    elif max_x - min_x == 1:
        print("2")
        return

    elif max_x - min_x == 0:
        print("0")
        return

if __name__ == "__main__":
    main()
