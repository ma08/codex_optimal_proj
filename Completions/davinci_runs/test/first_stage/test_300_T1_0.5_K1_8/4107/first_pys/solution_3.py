

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    #print(n,k,s)

    if n==1:
        print(0)
        return

    cost = 0
    for i in range(n):
        if s[i]=='1':
            cost += i+1
        else:
            if i+k<n and s[i+k]=='1':
                cost += i+1
            else:
                cost += (i+1)*2

    print(cost)

if __name__ == '__main__':
    main()