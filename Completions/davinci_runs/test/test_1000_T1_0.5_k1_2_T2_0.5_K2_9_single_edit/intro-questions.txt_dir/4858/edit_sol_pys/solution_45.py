
def main():
    M, N, C = input().split() # input three numbers
    M = int(M) # first number
    N = int(N) # second number
    first = [] # first list
    second = [] # second list
    for i in range(M): # loop for first list
        first.append(list(input())) # append the first list
    for i in range(M): # loop for second list
        second.append(list(input())) # append the second list
    for i in range(M): # loop for the first list
        for j in range(N): # loop for the first list
            if first[i][j] != C: # check if the first list is not equal to C
                first[i][j] = '.' # replace the first list with '.'
            else: # if the first list is equal to C
                first[i][j] = 'X' # replace the first list with 'X'
            if second[i][j] != C: # check if the second list is not equal to C
                second[i][j] = '.' # replace the second list with '.'
            else: # if the second list is equal to C
                second[i][j] = 'X' # replace the second list with 'X'
    for i in range(M): # loop for the second list
        for j in range(N): # loop for the second list
            if second[i][j] == 'X' and first[i][j] != 'X': # check if the second list is equal to 'X' and the first list is not equal to 'X'
                second[i][j] = '^' # replace the second list with '^'
    for i in range(M): # loop for the second list
        for j in range(N): # loop for the second list
            if second[i][j] == '^': # check if the second list is equal to '^'
                second[i][j] = '.' # replace the second list with '.'
            if second[i][j] == 'X': # check if the second list is equal to 'X'
                second[i][j] = C # replace the second list with C
    for i in range(M): # loop for the second list
        print(''.join(second[i])) # print the second list
    print()

if __name__ == '__main__':
    main()
