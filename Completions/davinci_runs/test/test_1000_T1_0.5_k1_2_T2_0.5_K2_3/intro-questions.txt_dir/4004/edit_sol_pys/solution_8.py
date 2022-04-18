

def main():
    n = int(input("Enter the number of elements: "))
    a = [int(i) for i in input("Enter the elements: ").split()]
    b = [a[i] for i in range(n) if a[i] % 2 == 0]
    print("Even numbers: ", b)

if __name__ == "__main__":
    main()
