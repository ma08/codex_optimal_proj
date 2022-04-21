
def main():
    A, B, C, D = map(int, input().split())
    print(max(A * C, A * D, B * C, B * D))

if __name__ == '__main__':
    main()
