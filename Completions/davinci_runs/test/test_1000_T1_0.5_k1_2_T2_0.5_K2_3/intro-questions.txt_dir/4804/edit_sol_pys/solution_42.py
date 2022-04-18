

import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":")
    if s > 3:
        print("2,1") # 2,1
        print("2,2") # 2,2
        print("3,2") # 3,2
        for i in range(4, int(s/2)+1):
            if s % i == 0 and s/i <= i: # if s is divisible by i and s/i is less than i
                print(i, int(s/i)) # then print i and s/i
            elif s % i <= i and s/i >= i: # if s is divisible by i and s/i is greater than i
                print(i, int(s/i)) # then print i and s/i
            elif s % i <= int(s/i) and s/i >= i: # if s is divisible by i and s/i is greater than i
                print(i, int(s/i)) # then print i and s/i
            elif s % i <= int(s/i) and s/i >= i+1: # if s is divisible by i and s/i is greater than i+1
                print(i, int(s/i)) # then print i and s/i

if __name__ == "__main__":
    main()
