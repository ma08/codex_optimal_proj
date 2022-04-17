
import sys
import sys

def main():
    N=int(sys.stdin.readline())
    A=[int(x) for x in sys.stdin.readline().split(' ')]
    B=[int(x) for x in sys.stdin.readline().split(' ')]
    ans=0
    for i in range(N): ans+=min(A[i],B[i])
    print(ans)

if __name__ == '__main__':
    main()
