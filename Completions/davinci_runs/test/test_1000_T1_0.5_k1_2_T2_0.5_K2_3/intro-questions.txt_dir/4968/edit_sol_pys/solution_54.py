

def main():
    n, s, r = map(int, input().split())
    damaged = set(map(int, input().split()))
    reserve = set(map(int, input().split()))
    count = 0
    for i in range(1, n+1):  # 一番左のseatから順にみていく
        if i in damaged:  # damaged seatがあるか
            if i-1 in reserve and i+1 in reserve:  # 左右両方がreserveにある場合(iを含む)
                reserve.remove(i-1)  # 左のseatをreserveから外す
                reserve.remove(i+1)  # 右のseatをreserveから外す
            elif i-1 in reserve:  # 左のみがreserveにある場合(iを含む)
                reserve.remove(i-1)  # 左のseatをreserveから外す
            elif i+1 in reserve:  # 右のみがreserveにある場合(iを含む)
                reserve.remove(i+1)  # 右のseatをreserveから外す
            else:
                count += 1  # 何もない場合、countに1足す
    print(count)

if __name__ == '__main__':
    main()
