

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = A + B
    AB.sort()
    print(AB[N-1])

if __name__ == "__main__":
    main()
