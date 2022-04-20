

def s(n):
   for i in range(n,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    print(t[:d][::-1], end="")
    d = s(n)
    print(t[d:], end="")

main()
