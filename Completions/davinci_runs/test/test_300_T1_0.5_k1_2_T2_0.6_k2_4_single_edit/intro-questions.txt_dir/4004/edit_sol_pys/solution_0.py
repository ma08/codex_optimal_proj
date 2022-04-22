

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    m = min(A)
    if sum(A) % n == 0: print(m)
    else: print(-1)

if __name__ == "__main__":
    main()
