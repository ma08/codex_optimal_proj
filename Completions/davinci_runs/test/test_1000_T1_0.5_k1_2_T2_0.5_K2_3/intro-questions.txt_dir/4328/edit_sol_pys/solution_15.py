

#-----Main Function-----

def main():
    #Get Input
    A, B, C = map(int, input().split())

    #Check if A is a divisor of C
    if C % A == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
