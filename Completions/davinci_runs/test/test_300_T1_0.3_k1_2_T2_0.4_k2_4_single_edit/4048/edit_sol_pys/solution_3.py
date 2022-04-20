

import sys

def main():
    n = int(sys.stdin.readline()) #reads the first line
    count = 0
    while n > 1: #while n is greater than 1
        if n % 2 == 0:
            n = n // 2 #divides n by 2
        else:
            n -= 1 #subtracts 1 from n
        count += 1 #adds 1 to the count
    print(count) #prints the count

if __name__ == '__main__':
    main()
