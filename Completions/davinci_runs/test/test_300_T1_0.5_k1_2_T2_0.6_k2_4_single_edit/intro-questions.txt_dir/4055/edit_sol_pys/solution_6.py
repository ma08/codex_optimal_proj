

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if (a[i] == 1):
            count = 0
        else:
            count += 1
            if (count > 5):
                print("#coderlifematters")
                break
    print(count)

if __name__ == "__main__":
    main()
