import sys

if __name__ == '__main__':
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        if n == 1:
            print("Not prime")
        elif n == 2:
            print("Prime")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")
