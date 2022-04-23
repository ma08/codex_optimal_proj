

def gcd(a, b):
   for i in range(a,b,-1):
       if a%i == 0 and b%i == 0:
           return i 

def main():
    n = int(input())
    t = input()
    d = gcd(n, len(t))
    print(t[d:], end="", sep="")
    print(t[:d][::-1], end="", sep="")

main()
