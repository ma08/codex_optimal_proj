
def main():
    n = int(input())
    names = [input() for _ in range(n)]
    for i in range(1, n):
        if names[i] < names[i - 1]:
            break
    else:
        print("INCREASING")
        return
    for i in range(1, n):
        if names[i] > names[i - 1]:
            break
    else:
        print("DECREASING")
        return
    print("NEITHER")


if __name__ == "__main__":
    main()
