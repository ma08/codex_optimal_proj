

n = int(input())  # number of elements
a = list(map(int, input().split()))  # list of elements

odds = 0  # sum of odd elements
evens = 0  # sum of even elements
count = 0  # number of equal sums

for i in range(n):  # summing odd and even elements
    if i % 2 == 0:  # if i is even
        evens += a[i]  # add element to evens
    else:
        odds += a[i]  # add element to odds

for i in range(n):  # subtracting one element
    if i % 2 == 0:  # if i is even
        evens -= a[i]  # subtract element from evens
    else:
        odds -= a[i]  # subtract element from odds
    if odds == evens:  # if sums are equal
        count += 1  # add 1 to count
    if i % 2 == 0:  # if i is even
        evens += a[i]  # add element to evens
    else:
        odds += a[i]  # add element to odds

print(count)
