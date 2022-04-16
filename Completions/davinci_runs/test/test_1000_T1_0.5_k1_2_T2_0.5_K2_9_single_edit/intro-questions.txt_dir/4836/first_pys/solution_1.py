

def main():
    n, c = map(int, input().split())
    w = list(map(int, input().split()))
    fruits = sorted(w)

    i = 0
    total = 0
    while i < n:
        if total + fruits[i] <= c:
            total += fruits[i]
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()