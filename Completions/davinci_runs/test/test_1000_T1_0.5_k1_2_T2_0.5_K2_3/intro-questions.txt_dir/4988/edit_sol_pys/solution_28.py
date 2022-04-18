def main():
    file = open("input.txt", "r")
    test_cases = int(file.readline())
    for i in range(test_cases):
        n = int(file.readline())
        print(n)
    file.close()


if __name__ == "__main__":
    main()
