

def main():
    n = int(input())
    for i in range(n):
        print(get_digit(i))

def get_digit(n):
    return str(n+1)[n]

if __name__ == "__main__":
    main()
