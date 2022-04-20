
import sys

def main():
    N = int(input())
    A = [int(x) for x in input().split(' ')]
    B = [int(x) for x in input().split(' ')]
    
    print(sum(min(A[i], B[i]) + min(A[i+1], B[i]) for i in range(N)))

if __name__ == '__main__':
    main()
