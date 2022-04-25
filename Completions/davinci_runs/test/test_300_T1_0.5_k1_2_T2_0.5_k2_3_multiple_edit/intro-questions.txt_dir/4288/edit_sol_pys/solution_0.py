
def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())  # input
        if a == b or b == c or a == c:  # condition
            print("Yes")  # output
        else:  # condition
            print("No")  # output

if __name__ == '__main__':
    main()
