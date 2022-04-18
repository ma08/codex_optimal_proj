
import os
def s(n):
   for i in range(n,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = s(n)
    print(t[d:], end="", flush=True)
    print(t[:d][::-1], end="", flush=True)

main()
