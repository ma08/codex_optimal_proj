

def main():
    white_x1, white_y1, white_x2, white_y2 = map(int, input().split())
    black1_x1, black1_y1, black1_x2, black1_y2 = map(int, input().split())
    black2_x1, black2_y1, black2_x2, black2_y2 = map(int, input().split())
    # print(white_x1, white_y1, white_x2, white_y2)
    # print(black1_x1, black1_y1, black1_x2, black1_y2)
    # print(black2_x1, black2_y1, black2_x2, black2_y2)

    if white_x1 >= black1_x2 or white_x2 <= black1_x1:
        if white_y1 >= black1_y2 or white_y2 <= black1_y1:
            if white_x1 >= black2_x2 or white_x2 <= black2_x1:
                if white_y1 >= black2_y2 or white_y2 <= black2_y1:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == "__main__":
    main()