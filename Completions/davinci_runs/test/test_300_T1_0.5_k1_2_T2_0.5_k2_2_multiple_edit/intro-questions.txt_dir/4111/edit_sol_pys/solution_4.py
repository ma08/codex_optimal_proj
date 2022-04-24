

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def find_good_candies(a, k):
    sum_odd, sum_even = 0
    for i in range(0,n):
        if a[i] >= k:
            if i%2 == 0:
                sum_even += 1
            else:
                sum_odd += 1
    return min(sum_odd, sum_even)

print(find_good_candies(a, k))
