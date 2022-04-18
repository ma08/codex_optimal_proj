

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[3]:
        print(a[0]**2)
    else:
        print(max(a[0] * a[1], a[2] * a[3]))

if __name__ == "__main__":
    main()
