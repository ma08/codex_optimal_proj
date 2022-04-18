
import sys

def s(n):
   for i in range(n,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = s(n)
    sys.stdout.write(t[d:])
    sys.stdout.write(t[:d][::-1])

main()
