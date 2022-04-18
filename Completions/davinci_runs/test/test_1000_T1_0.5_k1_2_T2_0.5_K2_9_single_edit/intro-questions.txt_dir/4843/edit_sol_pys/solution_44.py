
class Queens:
    def __init__(self):
        self.queens = []  # координаты королев в виде (x,y)

    def add_queen(self, queen):
        self.queens.append(queen)

    def check_queens(self):
        for queen in self.queens:
            if self.queens.count(queen) > 1:
                return False
        for queen1 in self.queens:
            for queen2 in self.queens:
                if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
                    if queen1 != queen2:
                        return False
        for queen1 in self.queens:
            for queen2 in self.queens:
                if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
                    if queen1 != queen2:
                        return False
        return True


def main():
    n = int(input())
    queens = Queens()
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        queens.add_queen((x, y))
    if queens.check_queens():
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == "__main__":
    main()
