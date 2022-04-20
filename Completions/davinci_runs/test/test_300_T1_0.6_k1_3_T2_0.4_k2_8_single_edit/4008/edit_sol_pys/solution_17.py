
def main():
    """Main Function"""
    _, k = map(int, input().split())
    arr = list(map(int, input().split()))
    color = [0] * 5001
    for i in arr:
        if color[i] == 0:
            color[i] = 1
        else:
            color[i] += 1
    for j in color:
        if j > k:
            print("NO")
            return
    print("YES")
    for i in arr:
        print(color[i], end=" ")

if __name__ == '__main__':
    main()
