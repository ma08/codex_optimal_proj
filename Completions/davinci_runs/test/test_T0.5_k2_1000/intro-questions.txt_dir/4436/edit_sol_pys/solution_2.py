

def main():
    n = int(input())
    for i in range(n):
        number = int(input())
        if number % 2 == 0 and number != 2:
            print("yes")
            for j in range(2, number+1):
                if number % j == 0:
                    print(j, end=" ")
                    number //= j
                    break
            print(number)
        else:
            print("no")


if __name__ == "__main__":
    main()
