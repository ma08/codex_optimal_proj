
def get_max_packages(n, k):
    max_packages = n
    for i in range(2, k+1):
        if n % i == 0:
            packages = n//i
            if packages > max_packages:
                max_packages = packages
    return max_packages
