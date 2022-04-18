import sys

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a
 
def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    lines = sys.stdin.readlines()
    for i in range(1, len(lines)):
        line = lines[i].strip()
        n,s = line.split()
        n,s = int(n),s[0]
        if s=='o':
            print(i,lcm(n//2,n//2+1)//n)
        elif s=='e':
            print(i,lcm(n//2,n//2-1)//n)

if __name__ == '__main__':
    main()
