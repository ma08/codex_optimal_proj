
def f(n):
    n = n + 1  # increment by 1
    while n % 10 == 0:  # if the last digit is 0
        n = n // 10  # remove the last digit
    return n

def main():
    n = int(input())
    memo = set()  # set of numbers we have seen so far
    while n not in memo:  # if we haven't seen this number before
        memo.add(n)  # add the number to the set
        n = f(n)
    print(len(memo))  # print the number of numbers we have seen so far

if __name__ == "__main__":
    main()
