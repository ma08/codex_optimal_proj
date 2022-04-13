
def main():
    K = int(input())
    desks = list(map(int, input().split()))  # Список массива чисел
    pos = 0
    passes = 0
    while pos < K:
        if desks[pos] == pos+1:  # Если номер стола равен номеру ученика
            pos += 1
        else:
            passes += 1
    print(passes)

if __name__ == '__main__':
    main()
