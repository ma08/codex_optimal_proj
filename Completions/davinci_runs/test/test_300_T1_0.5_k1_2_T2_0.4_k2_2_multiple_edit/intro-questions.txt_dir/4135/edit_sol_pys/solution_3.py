

def gcd(n,m):
   for i in range(n,0,-1):
       if n%i == 0 and m%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = gcd(n,len(t))
    print(t[d:], end="")
    print(t[:d][::-1], end="")

main()
