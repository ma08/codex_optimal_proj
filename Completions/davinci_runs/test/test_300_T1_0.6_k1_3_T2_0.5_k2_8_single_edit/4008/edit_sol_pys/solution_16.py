
def main():
    """Main Function"""
    _, k = map(int, input().split())
    arr = list(map(int, input().split()))
    color = [0] * 5001
    for i in range(len(arr)):
        if color[arr[i]] == 0:
            color[arr[i]] = 1
        else:
            color[arr[i]] += 1
    for i in color:
        if i > k:
            print("NO")
            return
    print("YES")
    for i in range(len(arr)):
        print(color[arr[i]], end=" ")

if __name__ == '__main__':
    main()
