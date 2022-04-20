

def answer(n, a):
    pass

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(answer(n, a))
