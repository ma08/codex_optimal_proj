

#-----main-----

a = list(map(int, input().split()))

#find the smallest number in the list
min = 100
for i in a:
    if i < min:
        min = i

#find the largest number in the list
max = 0
for i in a:
    if i > max:
        max = i

#find the sum of the list
sum = 0
for i in a:
    sum += i

#find the average of the list
avg = sum / len(a)

#find the median of the list
a.sort()
if len(a) % 2 == 0:
    median = (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2
else:
    median = a[len(a) // 2]

#find the mode of the list
mode = 0
for i in a:
    if a.count(i) > mode:
        mode = i

#find the range of the list
range = max - min

#find the variance of the list
variance = 0
for i in a:
    variance += (i - avg)**2
variance /= len(a)

#find the standard deviation of the list
stdev = variance**0.5

#find the sum of the squares of the list
sumsq = 0
for i in a:
    sumsq += i**2

#find the sum of the cubes of the list
sumsqc = 0
for i in a:
    sumsqc += i**3

#find the sum of the list
sum = 0
for i in a:
    sum += i

#find the sum of the reciprocals of the list
sumrec = 0
for i in a:
    sumrec += 1/i

#find the sum of the squares of the reciprocals of the list
sumsqrec = 0
for i in a:
    sumsqrec += 1/(i**2)

#find the sum of the cubes of the reciprocals of the list
sumsqcrec = 0
for i in a:
    sumsqcrec += 1/(i**3)

#find the sum of the nth powers of the list
n = 3
sumn = 0
for i in a:
    sumn += i**n

#find the sum of the nth roots of the list
n = 3
sumnroot = 0
for i in a:
    sumnroot += i**(1/n)

#find the sum of the nth powers of the reciprocals of the list
n = 3
sumnrec = 0
for i in a:
    sumnrec += 1/(i**n)

#find the sum of the nth roots of the reciprocals of the list
n = 3
sumnrootrec = 0
for i in a:
    sumnrootrec += 1/(i**(1/n))

#find the sum of the reciprocals of the nth powers of the list
n = 3
sumrecn = 0
for i in a:
    sumrecn += 1/(i**n)

#find the sum of the reciprocals of the nth roots of the list
n = 3
sumrecnroot = 0
for i in a:
    sumrecnroot += 1/(i**(1/n))

#find the sum of the reciprocals of the nth powers of the reciprocals of the list
n = 3
sumrecnrec = 0
for i in a:
    sumrecnrec += 1/(1/(i**n))

#find the sum of the reciprocals of the nth roots of the reciprocals of the list
n = 3
sumrecnrootrec = 0
for i in a:
    sumrecnrootrec += 1/(1/(i**(1/n)))

#find the sum of the reciprocals of the nth powers of the list
n = 3
sumrecn = 0
for i in a:
    sumrecn += 1/(i**n)

#find the sum of the reciprocals of the nth roots of the list
n = 3
sumrecnroot = 0
for i in a:
    sumrecnroot += 1/(i**(1/n))

#find the sum of the reciprocals of the nth powers of the reciprocals of the list
n = 3
sumrecnrec = 0
for i in a:
    sumrecnrec += 1/(1/(i**n))

#find the sum of the reciprocals of the nth roots of the reciprocals of the list
n = 3
sumrecnrootrec = 0
for i in a:
    sumrecnrootrec += 1/(1/(i**(1/n)))