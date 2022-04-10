

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    print(min([max(a[:i] + a[i+1:]) - min(a[:i] + a[i+1:]) for i in range(n)]))

if __name__ == "__main__":
    main()