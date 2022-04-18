

def main():
    n = int(input())
    d1, d2 = map(int, input().split())
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2 == d3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
