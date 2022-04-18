
n = int(input())
a = list(map(int, input().split()))

# find indices of all elements with value of 2
indices_2 = [i for i, x in enumerate(a) if x == 2]

# find indices of all elements with value of 4
indices_4 = [i for i, x in enumerate(a) if x == 4]

# find indices of all elements with value of 8
indices_8 = [i for i, x in enumerate(a) if x == 8]

# find indices of all elements with value of 16
indices_16 = [i for i, x in enumerate(a) if x == 16]

# find indices of all elements with value of 32
indices_32 = [i for i, x in enumerate(a) if x == 32]

# find indices of all elements with value of 64
indices_64 = [i for i, x in enumerate(a) if x == 64]

# find indices of all elements with value of 128
indices_128 = [i for i, x in enumerate(a) if x == 128]

# find indices of all elements with value of 256
indices_256 = [i for i, x in enumerate(a) if x == 256]

# find indices of all elements with value of 512
indices_512 = [i for i, x in enumerate(a) if x == 512]

# find indices of all elements with value of 1024
indices_1024 = [i for i, x in enumerate(a) if x == 1024]

# find indices of all elements with value of 2048
indices_2048 = [i for i, x in enumerate(a) if x == 2048]
