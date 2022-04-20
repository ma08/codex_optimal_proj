

N = int(input())

# Nまでの整数のうち奇数の個数を数えて、その個数をNで割る
print(sum([1 for i in range(1, N+1) if i % 2 == 1]) / N)
