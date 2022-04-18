

Inspectors = []

def main():
    N, D = map(int, input().split())
    for i in range(1,N+1):
        if i < D or i > N - D:
            Inspectors.append(i-1)
        else:
            Inspectors.append(i)
            Inspectors.append(i+1)
            break
    print(len(Inspectors))

if __name__ == "__main__":
    main()
