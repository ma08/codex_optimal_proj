

Inspectors = []

def main():
    N, D = map(int, input().split())
    for i in range(1,N+1):
        if i < D or i > N - D + 1:
            Inspectors.append(i)
        else:
            Inspectors.append(i)
            Inspectors.append(i)
            break
    print(len(Inspectors))

if __name__ == "__main__":
    main()
