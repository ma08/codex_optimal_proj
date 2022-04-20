

class Problem:
    def __init__(self):
        self.k = int(input())
        self.a, self.b = map(int, input().split()) # 入力をmapで組み込む
    
    def solve(self):
        if self.a % self.k == 0:
            print('OK')
        else:
            for i in range(self.a, self.b+1): # a~bまでの数字を繰り返す
                if i % self.k == 0:
                    print('OK')
                    return
            print('NG')

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    main()
