
#N = input()
#N = N.split(' ')
N = list(map(int, input().split()))

train = N[0] * N[1]
taxi = N[2]

print(train if train < taxi else taxi)