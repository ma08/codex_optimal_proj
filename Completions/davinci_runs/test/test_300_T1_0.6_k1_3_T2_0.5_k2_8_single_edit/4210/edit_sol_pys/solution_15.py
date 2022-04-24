

def main():
    n = int(input())
    a = list(map(int, input().split())
    a.sort()
    for i in a:
        if n != i:
            print(i)
            break

if __name__ == "__main__":
    main()
