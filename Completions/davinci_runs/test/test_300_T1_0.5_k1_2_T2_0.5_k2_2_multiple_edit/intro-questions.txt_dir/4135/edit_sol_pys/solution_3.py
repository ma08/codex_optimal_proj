

def s(n): # returns the number of characters in the first line
   for i in range(n, 0, -1):
       if n%i == 0:
           return i

def main():
    n = int(input())
    t = input()
    d = s(n)
    print(t[d:], end="") # prints the second line
    print(t[:d][::-1], end="") # prints the first line in reverse order

main()
