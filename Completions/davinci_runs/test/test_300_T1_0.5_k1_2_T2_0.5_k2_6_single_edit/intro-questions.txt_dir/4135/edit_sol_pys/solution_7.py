

def s(n):
   for i in range(n-1,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = t.replace(" ","")
    t = input()
    d = s(n)
    print(t[d:], end="")
    print(t[:d][::-1], end="")

main()
