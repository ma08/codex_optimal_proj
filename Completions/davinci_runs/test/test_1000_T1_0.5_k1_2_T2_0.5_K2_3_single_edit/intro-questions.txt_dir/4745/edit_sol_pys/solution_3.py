
def print_rangoli(size):
    # your code goes here
    for i in range(size):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))
    for i in range(n-1):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))
