
def main(): #function to call the program
    a, b = map(int, input().split())
    if a == 1 or b == 1: #if either input is 1
        print(a*b) #print the product
    elif a == 2: #if the first input is 2
        if b == 2 or b == 3 or b == 5 or b == 7: #if the second input is 2, 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 2, 3, 5 or 7
            print(-1) #print -1
    elif a == 3: #if the first input is 3
        if b == 2 or b == 3 or b == 5 or b == 7: #if the second input is 2, 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 2, 3, 5 or 7
            print(-1) #print -1
    elif a == 4: #if the first input is 4
        if b == 3 or b == 5 or b == 7: #if the second input is 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 3, 5 or 7
            print(-1) #print -1
    elif a == 5: #if the first input is 5
        if b == 2 or b == 3 or b == 5 or b == 7: #if the second input is 2, 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 2, 3, 5 or 7
            print(-1) #print -1
    elif a == 6: #if the first input is 6
        if b == 5 or b == 7: #if the second input is 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 5 or 7
            print(-1) #print -1
    elif a == 7: #if the first input is 7
        if b == 2 or b == 3 or b == 5 or b == 7: #if the second input is 2, 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 2, 3, 5 or 7
            print(-1) #print -1
    elif a == 8: #if the first input is 8
        if b == 3 or b == 5 or b == 7: #if the second input is 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 3, 5 or 7
            print(-1) #print -1
    elif a == 9: #if the first input is 9
        if b == 2 or b == 3 or b == 5 or b == 7: #if the second input is 2, 3, 5 or 7
            print(a*b) #print the product
        else: #if the second input is not 2, 3, 5 or 7
            print(-1) #print -1
    else: #if the first input is not 1, 2, 3, 4, 5, 6, 7, 8 or 9
        print(-1) #print -1
if __name__ == '__main__': #if the program is called from the command line
    main()
