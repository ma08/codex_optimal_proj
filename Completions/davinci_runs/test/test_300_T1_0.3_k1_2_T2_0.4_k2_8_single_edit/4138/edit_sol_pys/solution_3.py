

def main():
    n = int(input())
    for i in range(n):
        line = input().split()
        print(get_digit(int(line[0]), int(line[1]), int(line[2])))

def get_digit(a, b, k):
    return str(a ** b)[k-1]

if __name__ == "__main__":
    main()
