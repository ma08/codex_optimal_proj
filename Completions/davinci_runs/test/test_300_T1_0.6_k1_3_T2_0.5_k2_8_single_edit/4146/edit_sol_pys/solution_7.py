

def main():
    n = int(input())  # number of elements
    a = [int(x) for x in input().split()]  # list of elements
    a.sort()  # sort list
    n1 = a.count(a[0])  # count number of first element
    n2 = a.count(a[n-1])  # count number of last element
    if n1*2 == n:  # if first element is repeated for half of the list, then delete half of first element
        print(n//2-1)  # print half of the list
    elif n2*2 == n:  # if last element is repeated for half of the list, then delete half of first element
        print(n//2-1)  # print half of the list
    else:  # if neither first or last element is repeated for half of the list, then delete half of first and last element
        print(n-n1-n2)  # print half of first and half of last element

if __name__ == '__main__':
    main()
