

def chess_knight(h, w):
    if h == 1 or w == 1:
        return h * w
    elif h == 2 or w == 2:
        if h == 2:
            return 4 * ((w + 1) // 2)
        else:
            return 4 * ((h + 1) // 2)
    else:
        return (h * w + 1) // 2


if __name__ == '__main__':
    h = int(input())
    w = int(input())
    print(chess_knight(h, w))
