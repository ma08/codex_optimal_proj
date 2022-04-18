

def main():
    n, c = map(int, input().split())  # n, c = 5, 10
    w = list(map(int, input().split()))  # w = [1, 2, 3, 4, 5]
    fruits = sorted(w)  # fruits = [1, 2, 3, 4, 5]

    i = 0  # i = 0
    total = 0  # total = 0
    while i < n:
        if total + fruits[i] <= c:  # total + fruits[0] = 1 <= 10
            total += fruits[i]  # total = 1
            i += 1  # i = 1
        else:  # total + fruits[1] = 3 <= 10
            break  # total = 3

    print(i)  # print(2)


if __name__ == "__main__":
    main()
