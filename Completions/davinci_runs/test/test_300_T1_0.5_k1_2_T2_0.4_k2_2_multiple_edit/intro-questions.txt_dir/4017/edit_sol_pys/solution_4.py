
n = int(input())
a = list(map(int, input().split()))

# find indices of all elements with value of 2
indices_2 = [i for i, x in enumerate(a) if x == 2]

# find indices of all elements with value of 3
indices_3 = [i for i, x in enumerate(a) if x == 3]

# find indices of all elements with value of 4
indices_4 = [i for i, x in enumerate(a) if x == 4]

# find indices of all elements with value of 5
indices_5 = [i for i, x in enumerate(a) if x == 5]

# find indices of all elements with value of 6
indices_6 = [i for i, x in enumerate(a) if x == 6]
