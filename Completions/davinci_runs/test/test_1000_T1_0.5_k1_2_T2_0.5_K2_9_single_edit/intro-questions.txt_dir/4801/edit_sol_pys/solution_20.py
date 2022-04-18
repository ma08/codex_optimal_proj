

def main():
    n = int(input())  # number of elements in the sequence
    permutation = list(map(int, input().split()))  # read the permutation

    gis = [permutation[0]]  # create a list with the first element of the permutation

    for i in range(1, n):  # iterate from the second element to the last one
        if permutation[i] > gis[-1]:  # if the current element is greater than the last one in the list
            gis.append(permutation[i])  # add the current element to the list

    print(len(gis))  # print the length of the list
    print(*gis)  # print the list

if __name__ == '__main__':
    main()
