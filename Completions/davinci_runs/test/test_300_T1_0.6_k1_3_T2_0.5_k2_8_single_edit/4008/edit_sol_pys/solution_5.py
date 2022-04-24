
def main():
    """Main Function"""
    _, k = map(int, input().split())
    arr = list(map(int, input().split()))
    color = [0] * 5001 # สร้าง array ขนาด 5001 เพื่อเก็บค่าสี
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
