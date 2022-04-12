

def main():
    k = int(input("Enter the number of terms: ")) # k is the number of terms
    a, b = 0, 1
    for i in range(k): # i is the number of times the loop is run
        a, b = b, a+b
    print(a, b)

if __name__ == "__main__":
    main()
