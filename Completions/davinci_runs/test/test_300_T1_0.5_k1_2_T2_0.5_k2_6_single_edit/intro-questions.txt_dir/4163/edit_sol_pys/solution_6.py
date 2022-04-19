
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N-2):  
        if A[i] == A[i+1] and A[i+1] == A[i+2]:
            print("Yes")  
            return  
    print("No")  
    return

if __name__ == "__main__":
    main()
