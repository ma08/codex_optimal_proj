

def check_intersection(rect1, rect2):
    if rect1[0] > rect2[2] or rect1[2] < rect2[0]:
        return False
    if rect1[1] > rect2[3] or rect1[3] < rect2[1]:
        return False
    return True

def main():
    rect1 = [int(i) for i in input().split()]
    rect2 = [int(i) for i in input().split()]
    rect3 = [int(i) for i in input().split()]
    if check_intersection(rect1, rect2) or check_intersection(rect1, rect3) or check_intersection(rect2, rect3):
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()