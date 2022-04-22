

def main():
    N, K = map(int, input().split())
    S = input()
    print(S*(K//N) + S[:K%N])

if __name__ == "__main__":
    main()
