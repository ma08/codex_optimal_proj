

# Get input
L, R = map(int, input().split())    # 2020 2040

# Initialize variables
min_value = 2019

# Find minimum value
if R - L >= 2019:
    print(0)
else:
    for i in range(L, R):
        for j in range(i+1, R+1):
            value = (i * j) % 2019
            if value < min_value:
                min_value = value
print(min_value)
