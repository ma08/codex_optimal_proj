

#------------------------------------------------------------------------------#

def minDays(n,m,a):
    """
    Calculate the minimum number of days to complete the coursework, given
    the number of drinks, the number of pages, and the caffeine in each drink.
    """
    # Sort the caffeine levels, high to low
    a.sort(reverse=True)
    # Take the sum of the first m elements, since these are the ones that will
    # contribute to the coursework
    a = sum(a[:m])
    # If the sum is less than m, then the work cannot be completed
    if a < m:
        return -1
    # Else, the number of days is equal to the rounded-up quotient of the sum
    # and the number of pages
    return (a + m - 1) // m

#------------------------------------------------------------------------------#

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    print(minDays(n,m,a))

if __name__ == '__main__':
    main()