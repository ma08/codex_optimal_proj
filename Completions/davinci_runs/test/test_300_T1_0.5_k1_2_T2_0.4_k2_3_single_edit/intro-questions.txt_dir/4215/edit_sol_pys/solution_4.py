

def main():
    a, b = map(int, input().split())
#-----main-----

    if a <= b:
        print(0)
    else:
        print(a - b)


if __name__ == "__main__":
    main()
