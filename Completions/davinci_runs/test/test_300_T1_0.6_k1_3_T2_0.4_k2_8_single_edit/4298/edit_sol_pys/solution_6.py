

inspectors = []

def main():
    N, D = map(int, input().split())
    for i in range(1,N+1):
        if i < D or i > N - D:
            inspectors.append(i)
        else:
            inspectors.append(i)
            inspectors.append(i)
            break
    print(len(inspectors))

if __name__ == "__main__":
    main()
