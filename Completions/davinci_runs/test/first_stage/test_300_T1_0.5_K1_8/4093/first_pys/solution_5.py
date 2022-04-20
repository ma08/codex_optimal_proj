

def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        if n == 1:
            print(0)
        elif n == 2:
            print(2)
        elif n == 3:
            print(m-1)
        else:
            if m % 2 == 0:
                print(m - 1)
            else:
                print(m)

main()