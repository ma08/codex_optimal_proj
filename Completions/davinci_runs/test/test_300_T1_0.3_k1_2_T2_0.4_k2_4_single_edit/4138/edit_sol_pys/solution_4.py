

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_digit(n))

def get_digit(n):
    return str(n)[-1]

if __name__ == "__main__":
    main()
