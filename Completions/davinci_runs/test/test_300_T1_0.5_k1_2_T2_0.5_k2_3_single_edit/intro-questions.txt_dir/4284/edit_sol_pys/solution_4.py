

#-----Solution 1-----

#The solution is to iterate through the array and store the number of
#occurances of each number. If the number of occurances of a number is odd,
#then it is a number that cannot be paired.

#The number of unpaired numbers is the number of odd occurances.

def unpaired_numbers(n, arr):
    occurances = {}
    for i in arr:
        if i in occurances:
            occurances[i] += 1
        else:
            occurances[i] = 1
    num_unpaired = 0
    for i in occurances:
        if occurances[i] % 2 == 1:
            num_unpaired += 1
    return num_unpaired

q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(unpaired_numbers(n, arr))
