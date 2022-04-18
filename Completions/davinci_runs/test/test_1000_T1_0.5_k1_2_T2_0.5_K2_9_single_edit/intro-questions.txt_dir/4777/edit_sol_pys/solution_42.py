

def main():
    k = int(input())
    a, b = 1, 1
    for i in range(k):
        a, b = b, a+b
    print(a, b, sep=' ')

if __name__ == "__main__":
    main()
