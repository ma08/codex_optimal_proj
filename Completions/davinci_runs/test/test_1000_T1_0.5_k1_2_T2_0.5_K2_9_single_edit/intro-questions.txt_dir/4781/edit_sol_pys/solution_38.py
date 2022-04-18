def main():
    n = int(input())
    m = int(input())


    arr = []
    for _ in range(n):
        arr.append(input())

    for _ in range(m):
        t = input()
        for i in range(n):
            if t in arr[i]:
                print(i + 1)
                break
        else:
            print('NIET ZNALEZIONO')

main()
