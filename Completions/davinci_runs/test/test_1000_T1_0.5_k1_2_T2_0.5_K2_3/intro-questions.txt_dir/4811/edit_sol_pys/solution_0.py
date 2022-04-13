

def main():
    k = int(input())
    if k == 1:
        print("1 0")
    else:
        i = 2
        while i < k:
            i *= 2
        print("{} {}".format(i, i//2-1))

if __name__ == "__main__":
    main()
