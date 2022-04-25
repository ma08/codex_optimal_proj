

def s(n):
   for i in range(n,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = s(n) # d = gcd(n,len(t))
    print(t[d:], end="") # print the first part of the string
    print(t[:d][::-1], end="") # print the second part of the string

main()
