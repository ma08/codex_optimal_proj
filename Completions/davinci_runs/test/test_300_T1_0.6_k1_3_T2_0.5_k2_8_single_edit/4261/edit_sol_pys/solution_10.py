
def main():
    a, b, c = list(map(int, input().split()))
    print(c - min(a - b, c))

if __name__ == "__main__":
    main()
