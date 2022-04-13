def main():
    S = int(input())
    print(S, ":")
    for i in range(2, int(S / 2) + 1):
        if S % i == 0 and i >= S // i:
            print("{},{}".format(i, S // i))



if __name__ == "__main__":
    main()
