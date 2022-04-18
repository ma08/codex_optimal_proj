
def main():
    """Main Function"""
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == k:
        print("YES")
        for i in range(k):
            print(1, end=" ")
    else:
        color = [0] * 5001
        for i in arr:
            if color[i] == 0:
                color[i] = 1
            else:
                color[i] += 1
        for i in color:
            if i > k:
                print("NO")
                return
        print("YES")
        for i in arr:
            print(color[i], end=" ")

if __name__ == '__main__':
    main()
