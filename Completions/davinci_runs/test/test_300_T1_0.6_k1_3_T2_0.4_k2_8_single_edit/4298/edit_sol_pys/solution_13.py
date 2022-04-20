
inspectors = []

def main():
    n, d = map(int, input().split())
    for i in range(1, n+1):
        if i < d or i > n - d:
            inspectors.append(i)
        else:
            inspectors.append(i)
            inspectors.append(i)
            break
    print(len(Inspectors))

if __name__ == "__main__":
    main()
