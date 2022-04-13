

# SOLUTION for https://www.codechef.com/problems/XXOR

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(a[l - 1] ^ a[r - 1])

if __name__ == "__main__":
    main()
