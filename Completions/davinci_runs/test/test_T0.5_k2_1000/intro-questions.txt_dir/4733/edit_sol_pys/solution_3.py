import sys

def main():
    x = int(sys.stdin.readline()) # read the first line of the input
    shuffle = sys.stdin.readline().strip() # read the second line of the input
    if shuffle == 'out': # if the second line is 'out'
        if x % 2 == 0: # if the number is even
            print(x // 2) # print the number divided by 2
        else: # if the number is odd
            print((x + 1) // 2) # print the number plus 1 divided by 2
    elif shuffle == 'in': # if the second line is 'in'
        if x % 2 == 0: # if the number is even
            print(x - 1) # print the number minus 1
        else: # if the number is odd
            print(x) # print the number
main()
