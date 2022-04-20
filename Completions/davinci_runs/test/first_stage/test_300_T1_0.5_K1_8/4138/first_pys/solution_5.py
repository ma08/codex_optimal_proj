

#We can use the formula for the sum of an arithmetic progression
#to get the position of the digit in the sequence
#(i.e. the sum of the numbers from 1 to n)

def sumOfAP(n):
    return n*(n+1)/2

def getDigit(k):
    n = 1
    while(sumOfAP(n) < k):
        n += 1
    return k - sumOfAP(n-1)

q = int(input())
for i in range(q):
    k = int(input())
    print(int(str(n)[int(getDigit(k))-1]))