

#%%
# Read input
A, B = map(int, input().split())

#%%
# Initialize variables
price = -1

#%%
# Check prices until a valid one is found
i = 1
while price == -1:
    tax8 = int(i * 0.08)
    tax10 = int(i * 0.1)
    if tax8 == A and tax10 == B:
        price = i
    i += 1

#%%
# Print result
print(price)