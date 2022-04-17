

def get_divisor(n):
   for i in range(n,0,-1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = get_divisor(n)
    print(t[d:], end="")
    print(t[:d][::-1], end="")

main()
