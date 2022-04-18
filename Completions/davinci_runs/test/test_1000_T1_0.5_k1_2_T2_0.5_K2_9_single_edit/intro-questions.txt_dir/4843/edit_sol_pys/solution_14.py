
class Queens:
    def __init__(self, n):
        self.n = n
        self.queens = []
        for i in range(n):
            self.queens.append([])

    def add_queen(self, x, y):
        self.queens[x].append(y)

    def check_queens(self):
        for i in range(self.n):  # check if there are more than 1 queen in a row
            if len(self.queens[i]) > 1:  # if there are more than 1 queen
                return False
        for i in range(self.n):  # check if there are more than 1 queen in a column
            for j in range(self.n):
                if len(self.queens[j]) == 1 and self.queens[j][0] == i:  # if there is a queen
                    break
                if j == self.n - 1:  # if there are no queens
                    return False
        for i in range(self.n):  # check if there are more than 1 queen in a diagonal
            for j in range(self.n):
                if len(self.queens[j]) == 1:  # if there is a queen
                    x = j
                    y = self.queens[j][0]
                    for k in range(self.n):
                        if len(self.queens[k]) == 1:  # if there is a queen
                            if abs(x - k) == abs(y - self.queens[k][0]):  # if the queens are in the same diagonal
                                return False
        return True


def main():
    n = int(input())
    queens = Queens(n)
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        queens.add_queen(x, y)
    if queens.check_queens():
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == "__main__":
    main()
