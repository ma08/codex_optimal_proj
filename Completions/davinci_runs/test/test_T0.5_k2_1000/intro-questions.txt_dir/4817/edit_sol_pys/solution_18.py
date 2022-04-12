

def next_largest(x):
    # Start with the largest number that can be formed using the digits of x
    n = 10 ** (len(str(x)) - 1)

    # Find the largest number that can be formed using the digits of x
    for i in range(9, 0, -1):
        if str(i) in str(x):
            n += i * 10 ** (len(str(x)) - str(x).index(str(i)) - 1)
            break

    # Find the next largest number using the same digits
    for i in range(9, 0, -1):
        if str(i) in str(n):
            n += i * 10 ** (len(str(x)) - str(n).index(str(i)) - 1)
            break

    # If the number is larger than x, print it. Otherwise, print 0.
    if n > x:
        print(n)
    else:
        print(0)


next_largest(int(input()))
