

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

if numbers[0] == 0:
    print("impossible")
else:
    print(numbers[0]/n)
