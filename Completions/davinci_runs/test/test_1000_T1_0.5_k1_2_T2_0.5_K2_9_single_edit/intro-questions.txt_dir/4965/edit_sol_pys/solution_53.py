

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int,input("Enter the elements: ").split()))
    arr.sort()
    print("The sorted array is: ",*arr)

if __name__ == "__main__":
    main()
