


with open("input.txt", "r") as f:
    N, W, H = map(int, f.readline().split())  # читаем данные из файла
    for i in range(N):
        if int(f.readline()) <= max(W, H):
            print("DA")
        else:
            print("NE")
