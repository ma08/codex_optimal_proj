

def main():
    f_in = open("f.in", "r") # open file for reading
    n = int(f_in.readline()) # read first line
    print(count_reachable(n)) # print output
# count number of reachable numbers

def count_reachable(n):
    if n == 1: # base case
        return 2
    return count_reachable(n-1) + is_reachable(n-1, n) # recursive call
# check if n is reachable from m

def is_reachable(n, m):
    if n == m: # base case
        return 1
    if n < 1: # base case
        return 0
    if n % 10 == 0: # recursive call
        return is_reachable(n//10, m)
    return is_reachable(n-1, m) # recursive call

if __name__ == "__main__":
    main()
