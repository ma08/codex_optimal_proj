

def main():
    n = int(input())  # number of elements
    a = [int(x) for x in input().split()]  # list of elements
    a.sort()  # sort list
    if a[-1] - a[0] > 1:  # check if difference between first and last elements is bigger than 1
        print("NO")  # if yes, print no
    else:  # else
        print("YES")  # print yes


main()  # call main function
