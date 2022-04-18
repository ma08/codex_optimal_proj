

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]

    print(len(set(S) - set(T)))

if __name__ == '__main__':
    main()
