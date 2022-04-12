

def main():
    n = int(input())  # n is the number of integers
    integers = input().split()  # integers is a list of strings
    for i in range(n):  # i goes from 0 to n-1
        if integers[i] != 'mumble' and int(integers[i]) != i+1:  # integers[i] is a string
            print("something is fishy")  # print this line and return
            return  # return from the function
    print("makes sense")  # print this line

main()
