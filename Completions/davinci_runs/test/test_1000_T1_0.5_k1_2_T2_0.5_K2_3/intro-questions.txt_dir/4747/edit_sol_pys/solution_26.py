
import sys

def main():
    n, k = sys.stdin.readline().split() # read inputs
    n = int(n)
    k = int(k)

    print(calculate(n,k)) # call function

def calculate(n,k):
    if k == 1: # base case
        return (n+1)/2
    else: # recursive case
        return (n+1)/2 + ((n-1)/n)*(k-1)*calculate(n-1,k-1)

main()
