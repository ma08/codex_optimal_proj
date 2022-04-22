

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)

    if n == 2:
        print(0)
        return
    if a_sorted[0] + 1 == a_sorted[1]:
        print(a_sorted[-1] - a_sorted[1])
        return
    if a_sorted[-1] - 1 == a_sorted[-2]:
        print(a_sorted[-1] - a_sorted[0])
        return
    print(min(a_sorted[-1] - a_sorted[1], a_sorted[-2] - a_sorted[0]))


if __name__ == "__main__":
    main()
