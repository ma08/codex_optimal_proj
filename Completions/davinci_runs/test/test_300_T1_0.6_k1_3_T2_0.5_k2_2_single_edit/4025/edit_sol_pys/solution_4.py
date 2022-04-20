

def main():
    a, b, c, k = [int(x) for x in input().split()]

    if a + b + c >= k:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
