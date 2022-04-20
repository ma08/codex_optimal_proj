

#main function
def main():
    #input
    N = int(input())

    #output
    if N % 2 == 0 or N % 3 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()