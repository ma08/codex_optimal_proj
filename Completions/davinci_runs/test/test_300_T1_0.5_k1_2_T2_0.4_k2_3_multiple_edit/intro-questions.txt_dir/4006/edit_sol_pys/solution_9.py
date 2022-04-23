
def f(n):
    n += 1
    while n % 10 == 0:
        n = n // 10
    return n

def main():
    n = int(input())
    memo = set() # memo is a set
    while n not in memo: # if n is not in memo
        memo.add(n) # add n to memo
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
