# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print "{0:>{width}d} {0:>{width}o} {0:>{width}X} {0:>{width}b}".format(i, width=len(bin(number)[2:]))


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
