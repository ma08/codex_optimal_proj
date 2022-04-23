

n = int(input())  # number of elements in list
a = list(map(int, input().split()))  # list of elements in list

odds = 0  # sum of odd elements in list
evens = 0  # sum of even elements in list
count = 0  # number of equal sums of odds and evens

for i in range(n):  # sum of odd and even elements in list
    if i % 2 == 0:  # if i is even
        evens += a[i]  # add element to evens in list
    else:
        odds += a[i]  # add element to odds

for i in range(n):  # subtracting one element in list
    if i % 2 == 0:  # if i is even
        evens -= a[i]  # subtract element from evens in list
    else:
        odds -= a[i]  # subtract element from odds in list
    if odds == evens:  # if sums of odds and evens in list are equal
        count += 1  # add 1 to count
    if i % 2 == 0:  # if i is even
        evens += a[i]  # add element to evens in list
    else:
        odds += a[i]  # add element to odds in list

print(count)
