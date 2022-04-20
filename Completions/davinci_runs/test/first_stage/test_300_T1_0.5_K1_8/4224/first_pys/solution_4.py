

import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    count = 0
    # Check if any element is divisible by 2
    while(any(x%2 == 0 for x in a)):
        # Check if any element is divisible by 4
        if(any(x%4 == 0 for x in a)):
            # Divide all elements by 2
            a = list(map(lambda x: x/2, a))
            count += 1
        else:
            # Divide all elements by 2 except for the first one
            for i in range(1, N):
                a[i] = a[i]/2
            count += 1
    print(count)

if __name__ == '__main__':
    main()