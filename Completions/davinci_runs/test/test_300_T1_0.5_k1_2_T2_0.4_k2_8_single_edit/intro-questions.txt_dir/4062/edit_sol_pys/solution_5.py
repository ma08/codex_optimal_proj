

def main():
    a, b, c, d = map(int, input().split())  # ε₯ε
    print(max(a * c, a * d, b * c, b * d))  # εΊε

if __name__ == '__main__':
    main()
