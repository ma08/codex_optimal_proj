def main():  
    n = int(input())
    print(solve(n))
    
def solve(n):
    # This is the solution to the problem, but it is too slow.
    # def is_prime(num):
    #     if num % 2 == 0 and num > 2: 
    #         return False
    #     return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))
    # return sum(1 for i in range(2, n + 1) if is_prime(i))
    # Instead, use the sieve of Eratosthenes
    nums = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if nums[p] == True:
            for i in range(p * 2, n + 1, p):
                nums[i] = False
        p += 1
    return sum(1 for i in range(2, n + 1) if nums[i])
        
if __name__ == "__main__":  
    main() 
