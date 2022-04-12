#!/usr/bin/env python3

C, K = map(int, input().split()) #C is the number, K is the number of digits

for i in range(K, 10): #i is the number of digits
    if C % (10**i) < 5*(10**(i-1)): #if the last digit is less than 5
        C = C - C % (10**i) #remove the last digit
    else:
        C = C - C % (10**i) + 10**i

print(C)
