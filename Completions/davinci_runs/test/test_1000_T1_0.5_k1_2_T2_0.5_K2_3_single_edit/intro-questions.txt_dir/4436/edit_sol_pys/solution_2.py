

def main():
    n = int(input())
    for i in range(0, n):
        number = int(input())
        if number % 2 == 0:
            print("YES")
            for j in range(2, number + 1):
                if number % j == 0:
                    print(j, end=" ")
                    number //= j
                    break
            print(number)
        else:
            print("NO")


if __name__ == "__main__":
    main()
