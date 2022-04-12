

def main():
    k = int(input("Enter the number of terms: "))
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
        print(a, b)

if __name__ == "__main__":
    main()
