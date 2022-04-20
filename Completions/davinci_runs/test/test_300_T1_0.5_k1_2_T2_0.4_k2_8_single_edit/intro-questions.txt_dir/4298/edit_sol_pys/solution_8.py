
import fractions

def main():
    N = int(input())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(N):
        gcd = fractions.gcd(gcd, A[i])
    print(gcd)

if __name__ == "__main__":
    main()
