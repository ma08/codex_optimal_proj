

N = int(input()) # число элементов
A = [int(i) for i in input().split()] # список элементов

for i in range(N):
    print(A.index(i+1)+1, end=' ') # вывод индекса элемента 
