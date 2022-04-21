

def main():
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    max_a = max(a)
    max_b = max(b)

    if max_a < max_b:
        print(0)
    else:
        min_b = min(b)
        count = 0
        for j in range(len(a)):
            if a[j] > min_b:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
