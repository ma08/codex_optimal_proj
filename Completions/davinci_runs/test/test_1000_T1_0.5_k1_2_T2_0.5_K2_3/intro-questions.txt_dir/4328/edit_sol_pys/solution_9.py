

#-----main function-----

def main():
    #get input for N
    N = int(input())

    A = list(map(int, input().split()))

    #get input for M
    M = int(input())
    B = list(map(int, input().split()))

    #initialize the dictionary.
    dic = {}

    #add values to the dictionary
    for i in A:
        dic[i] = 1

    #check if the values in B are in the dictionary
    for j in B:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

    #check if the values in the dictionary are greater than 1
    for k in dic:
        if dic[k] > 1:
            print(k)

if __name__ == '__main__':
    main()
