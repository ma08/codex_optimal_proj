
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
    flag = True
    for i in color:
        if i > k:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
    for i in arr:
        print(color[i], end=" ")

if __name__ == '__main__':
    main()
