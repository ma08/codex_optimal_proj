

def main():
    n = int(input())  # get the number of rows and columns
    i = 0
    j = 0
    arr = []  # create an empty array
    while i < n:
        arr.append(list(map(int, input().split())))  # get the array from the input
        i += 1
    res = [0] * n  # create a result array with zeros
    while j < n:
        res[j] = arr[j][0]  # fill the result array with the first column of the input array
        j += 1
    i = 1
    while i < n:
        res[i] = arr[0][i]  # fill the result array with the first row of the input array
        i += 1
    i = 1
    while i < n:
        j = 1
        while j < n:
            if i != j:
                res[i] = res[i] ^ arr[i][j]  # XOR the result array with the rest of the input array
            j += 1
        i += 1
    print(*res)  # print the result array

if __name__ == "__main__":
    main()
