

def main():
    r, n = map(int, input().split())  # r - количество комнат, n - количество забронированных комнат.
    booked = set()
    for _ in range(n):
        booked.add(int(input()))  # добавляем номера забронированных комнат в множество.
    for i in range(1, r+1):
        if i not in booked:  # если номер комнаты не входит в множество забронированных комнат, то выводим его.
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
