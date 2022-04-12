
class Queens:
    def __init__(self, n):
        self.n = n
        self.queens = []
        self.queens = [[] for i in range(n)]

    def add_queen(self, x, y):
        self.queens[x].append(y)

    def check_queen(self):
        for x in range(self.n):
            if len(self.queens[x]) > 1:
                return False  # проверка на одну королеву в строке
        for y in range(self.n):
            for x in range(self.n):
                if len(self.queens[x]) == 1 and self.queens[x][0] == y:
                    break  # проверка на одну королеву в столбце
                if x == self.n - 1:
                    return False  # проверка на одну королеву в столбце
        for y in range(self.n):
            for x in range(self.n):
                if len(self.queens[x]) == 1:
                    for k in range(self.n):
                        if len(self.queens[k]) == 1:
                            if abs(x - k) == abs(y - self.queens[k][0]):
                                return False  # проверка на одну королеву на диагонали
        return True


def main():
    n = int(input())
    queens = Queens(n)
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        queens.add_queen(x, y)
    if queens.check_queen():
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == "__main__":
    main()
