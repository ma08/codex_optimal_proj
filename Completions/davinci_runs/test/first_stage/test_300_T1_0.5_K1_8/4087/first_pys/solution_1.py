

def main():
    a = int(input())

    if a % 4 == 0:
        print(a)
    else:
        print(a + (4 - a % 4))

if __name__ == "__main__":
    main()