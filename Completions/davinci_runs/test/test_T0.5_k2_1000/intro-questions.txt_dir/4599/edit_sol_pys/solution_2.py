

def main():
    n = int(input())
    a = list(map(int, input().split()))

    Alice = 0
    Bob = 0
    for i in range(n):
        if i % 2 == 0:
            Alice += a[i]
        else:
            Bob += a[i]

    print(Alice - Bob)

if __name__ == "__main__":
    main()
