

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        n = str(n)
        for i in range(len(n)):
            if n[i] == '0':
                print(i + 1)
                return
        print(-1)

if __name__ == "__main__":
    main()
