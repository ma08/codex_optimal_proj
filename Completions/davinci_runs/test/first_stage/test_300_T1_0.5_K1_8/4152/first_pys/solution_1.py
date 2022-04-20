

#-----Solution-----

#This is a very simple problem.
#First we take the input, and we make a list of all the powers of two up to $10^9$.
#Then we check if each element in the input list is in the list of powers of two.
#If it is, we don't have to delete it. Otherwise, we have to delete it.

#We make a list of all the powers of two up to $10^9$.
powers_of_two = []
for i in range(30):
    powers_of_two.append(2**i)

#We take the input.
n = int(input())
a = list(map(int, input().split()))

#We check how many elements we have to delete.
ans = 0
for i in range(n):
    if a[i] not in powers_of_two:
        ans += 1

#We print the answer.
print(ans)