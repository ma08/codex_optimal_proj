

import sys

def main():
    count = 0
    for i in range(1,int(sys.stdin.readline())+1):
        if i%2 == 1:
            count+=1
    print(count/(int(sys.stdin.readline())))

if __name__ == '__main__':
    main()