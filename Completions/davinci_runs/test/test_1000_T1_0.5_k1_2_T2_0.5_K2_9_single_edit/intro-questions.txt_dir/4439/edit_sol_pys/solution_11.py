

def main():
    a, b, c = map(int, input().split())

    print(c // min(a, b))

if __name__ == "__main__":
    main()
