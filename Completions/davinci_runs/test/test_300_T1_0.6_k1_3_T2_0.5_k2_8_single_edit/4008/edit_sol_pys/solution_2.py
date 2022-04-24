
def main():
    """Main Function"""
    k = int(input())
    arr = list(map(int, input().split()))
    color = [0] * 5001
    for i in arr:
        if color[i] == 0:
            color[i] = 1
        else:
            color[i] += 1
    for i in color:
        if i > k and i != 0:
            print("NO")
            return
    print("YES")
    for i in arr:
        print(color[i], end=" ")

if __name__ == '__main__':
    main()
