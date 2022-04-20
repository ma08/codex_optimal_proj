

def main():
    n = int(input())
    arr = input().split()

    for i in range(n):
        if arr[i] == '0':
            print(0)
        else:
            print(1)

    print(arr)


main()
