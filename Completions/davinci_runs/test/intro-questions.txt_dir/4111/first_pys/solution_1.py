

def solve(n, candy):
    # find the even and odd sums of the candies
    even_sum = 0
    odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            even_sum += candy[i]
        else:
            odd_sum += candy[i]
    # count the number of good candies
    c = 0
    if even_sum == odd_sum:
        c = 1
    # check the remaining candies
    for i in range(1, n-1):
        # if even sum is greater
        if even_sum > odd_sum:
            even_sum -= candy[i-1]
            odd_sum += candy[i-1]
            if even_sum == odd_sum:
                c += 1
        # if odd sum is greater
        else:
            odd_sum -= candy[i-1]
            even_sum += candy[i-1]
            if even_sum == odd_sum:
                c += 1
    return c

if __name__ == '__main__':
    n = int(input())
    candy = list(map(int, input().split()))
    print(solve(n, candy))