

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        n = str(n)
        for i in range(len(n)):
            if n[i] == '2' or n[i] == '5':
                print(i)
                return
        print(-1)

if __name__ == "__main__":
    main()
