

def main():
    n = list(map(int, input().split()))
    n.sort()
    if n[0] == n[1] == n[2] == n[3]:
        print(n[0]**2)
    else:
        print(max(n[0] * n[1], n[2] * n[3]))

if __name__ == "__main__":
    main()
