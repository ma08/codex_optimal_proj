
<<<<<<< HEAD

n = int(input())
a = [int(i) for i in input().split()]

a.sort()

count = 1
for i in range(1,n):
    if a[i] != a[i-1]:
        count += 1

=======
print("hello World")
>>>>>>> 0a4c7f2e15aab7b6d8edf38b7db8b8894ecf7a41
print(count)
