

def main():
    k = int(input())
    a, b = map(int, input().split())
    if b//k >= a//k:
        print("OK")
    else:
        print("NG")

if __name__ == "__main__":
    main()