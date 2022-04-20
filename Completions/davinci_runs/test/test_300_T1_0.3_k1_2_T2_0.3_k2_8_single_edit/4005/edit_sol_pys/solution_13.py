

def main():
    x1, y1, x2, y2 = map(int, input().split())  # rectangle 1
    x3, y3, x4, y4 = map(int, input().split())  # rectangle 2
    x5, y5, x6, y6 = map(int, input().split())  # rectangle 3

    if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:  # check if rectangle 1 and 2 are not overlapping
        if x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:  # check if rectangle 1 and 3 are not overlapping
            print("YES")  # if both are not overlapping, print YES
        else:  # if any of them are overlapping, print NO
            print("NO")  # if any of them are overlapping, print NO
    else:  # if any of them are overlapping, print NO
        print("NO")  # if any of them are overlapping, print NO

if __name__ == "__main__":
    main()
