

Inspectors = []

def main():
    N, D = map(int, input().split())
    for i in range(1, N + 1):
        Inspectors.append(i)
        if D < i < N - D:
            Inspectors.append(i)
    print(len(Inspectors))

if __name__ == "__main__":
    main()
