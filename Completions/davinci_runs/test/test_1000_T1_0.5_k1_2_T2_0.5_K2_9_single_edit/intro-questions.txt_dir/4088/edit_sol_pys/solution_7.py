

def main():
    # read the number of elements
    n = int(input())

    # read the elements
    a = list(map(int, input().split()))

    # find the maximum element
    max_elem = max(a)

    # print the result
    print(max_elem)

if __name__ == "__main__":
    main()
