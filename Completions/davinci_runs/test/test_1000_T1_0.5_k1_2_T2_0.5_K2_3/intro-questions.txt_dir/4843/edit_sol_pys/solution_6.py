

class Queens(object):
    def __init__(self, n, m):
        self.n = n  # размер доски
        self.m = m  # количество ферзей
        self.queens = []
        for i in range(n):
            self.queens.append([])

    def add_queen(self, x, y):  # добавление ферзя в список
        self.queens[x].append(y)  # ключ - номер строки, значение - номер столбца

    def check_queens(self):  # проверка ферзей на корректность расположения
        for i in range(self.n):
            if len(self.queens[i]) > 1:  # проверяем на одновременное нахождение в одной строке
                return False
        for i in range(self.n):
            for j in range(self.n):
                if len(self.queens[j]) == 1 and self.queens[j][0] == i:  # проверяем на одновременное нахождение в одном столбце
                    break
                if j == self.n - 1:  # если ни один ферзь не находится в столбце, то возвращаем False
                    return False
        for i in range(self.n):
            for j in range(self.n):
                if len(self.queens[j]) == 1:
                    x = j
                    y = self.queens[j][0]
                    for k in range(self.n):
                        if len(self.queens[k]) == 1:
                            if abs(x - k) == abs(y - self.queens[k][0]):  # проверяем на одновременное нахождение на диагонали
                                return False
        return True


def main():
    n, m = [int(j) for j in input().split()]
    queens = Queens(n, m)
    for i in range(m):
        x, y = [int(j) for j in input().split()]
        queens.add_queen(x - 1, y - 1)
    if queens.check_queens():
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == "__main__":
    main()
