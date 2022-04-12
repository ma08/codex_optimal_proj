# fix syntax errors

c, k = map(int, input().split()) # c is the price of the item, k is the number of digits after the decimal point

print((c + 5*10**k - 1)//(10**k) * 10**k)
