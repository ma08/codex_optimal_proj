

def main():
    n = int(input())
    i = 0
    arr = []
    while i < n:
        arr.append(list(map(int, input().split())))
        i += 1
    print(arr)

if __name__ == "__main__":
    main()
