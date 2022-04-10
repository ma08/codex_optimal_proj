

a = list(map(int, input().split()))

# Check if there is an even number
if len(list(filter(lambda x: x % 2 == 0, a))) > 0:
    print(1)
else:
    print(0)