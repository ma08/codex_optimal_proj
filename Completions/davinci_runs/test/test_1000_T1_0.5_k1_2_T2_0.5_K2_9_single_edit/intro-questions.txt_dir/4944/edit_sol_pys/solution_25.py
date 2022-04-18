

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter element " + str(i+1) + " : ")))
    print(arr)

if __name__ == "__main__":
    main()
