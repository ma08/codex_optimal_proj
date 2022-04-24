

class Problem:
    def __init__(self):
        self.__k = int(input())
        self.__a, self.__b = map(int, input().split())
    
    def solve(self):
        if self.__a % self.__k == 0:
            print('OK')
        else:
            for i in range(self.__a, self.__b+1):
                if i % self.__k == 0:
                    print('OK')
                    return
            print('NG')

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    main()
