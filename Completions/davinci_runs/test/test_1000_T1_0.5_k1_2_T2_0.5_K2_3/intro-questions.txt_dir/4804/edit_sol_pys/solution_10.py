

def main():
    s = int(input())
    print(s, ":")

    if s % 2 == 0:
        for i in range(2, int(s/2)+1):
            if s % i == 0:
                print(i, int(s/i), end="")
    else:
        for i in range(2, int(s/2)+2):
            if s % i == 0:
                print(i, int(s/i), end="")

if __name__ == "__main__":
    main()
