
def main():
    A, B, C, D = map(int, input().split())  # A, B, C, D = [int(input()) for i in range(4)]
    print(max(A * C, A * D, B * C, B * D))  # print(max(A*C, A*D, B*C, B*D))

if __name__ == '__main__':
    main()
