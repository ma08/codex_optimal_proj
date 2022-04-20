

#-----main-----

#read input
a,b,x = list(map(int, input().split()))

#calculate price
def price(n):
    return a * n + b * len(str(n))

#calculate maximum integer that can be bought
def max_integer(x):
    #define upper limit
    upper = 10 ** 9
    #define lower limit
    lower = 0
    #define middle
    middle = upper // 2
    #if price(middle) is less than x, lower limit becomes middle
    while price(middle) >= x:
        upper = middle
        middle = (upper + lower) // 2
    #if price(middle) is greater than x, upper limit becomes middle
    while price(middle) < x:
        lower = middle
        middle = (upper + lower) // 2
    #return middle
    return middle

#print
print(max_integer(x))