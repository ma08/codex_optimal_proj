

def main():
    k = int(input("Enter a number: "))
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
    print("a = ", a, "b = ", b)

if __name__ == "__main__":
    main()
