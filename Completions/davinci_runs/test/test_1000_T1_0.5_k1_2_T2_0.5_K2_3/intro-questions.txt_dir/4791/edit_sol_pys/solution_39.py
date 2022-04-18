

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(max(a[0]*a[1], a[2]*a[3]))

if __name__ == "__main__":
    main()
