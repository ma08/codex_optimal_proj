
import sys

def check(n):
    n = str(n)
    if len(n) != 6:
        return False
    else:
        for i in range(len(n)):
            if n[i] == '0':
                return False 
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i] == n[j]:
                    return False
        for i in range(len(n)):
            if int(n) % int(n[i]) != 0:
                return False 
        return True

def main():
    L, H = map(int, sys.stdin.readline().split())
    count = 0
    for i in range(L, H+1):
        if check(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
