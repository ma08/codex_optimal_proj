

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in numbers:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

if __name__ == '__main__':
    main()