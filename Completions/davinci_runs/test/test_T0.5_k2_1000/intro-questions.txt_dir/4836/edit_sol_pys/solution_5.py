


def main():
    n, c = map(int, input().split())
    w = list(map(int, input().split()))
    weights = sorted(w)

    i = 0
    total = 0
    while i < n:
        if total + weights[i] <= c:
            total += weights[i]
            i += 1

        else:
            break

    print(i)

if __name__ == "__main__":
    main()
