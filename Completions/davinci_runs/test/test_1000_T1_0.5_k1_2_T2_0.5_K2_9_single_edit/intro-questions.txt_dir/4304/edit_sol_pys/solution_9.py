

def main():
    a, b = map(int, input().split())
    print(b-a-1 if a != b else 0)

if __name__ == '__main__':
    main()
