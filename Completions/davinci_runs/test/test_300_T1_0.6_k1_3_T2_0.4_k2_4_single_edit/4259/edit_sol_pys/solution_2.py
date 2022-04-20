

class Problem:
    def __init__(self):
        self.k, self.a, self.b = map(int, input().split())
        self.a, self.b = map(int, input().split())
    
    def solve(self):
        if self.a % self.k == 0:
            print('OK')
        else:
            for i in range(self.a, self.b+1):
                if i % self.k == 0:
                    print('OK')
                    return
            print('NG')

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    main()
