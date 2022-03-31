

# SOLUTION
# This is a really interesting problem.
# The idea is to find the smallest repeating unit of the string t.
# This can be done by finding the smallest length of a prefix of t that is a suffix of t as well.
# Then, we just need to repeat this prefix k times.

# The function to find the smallest repeating unit of t.
# This function is O(n^2) in the worst case.
def findSmallestRepeatingUnit(t):
    n = len(t)
    for i in range(n//2, 0, -1):
        if t[:i] == t[n-i:]:
            return t[:i]
    return t

# The main function that prints the result.
def main():
    n, k = map(int, input().split())
    t = input()
    print(findSmallestRepeatingUnit(t) * k)

# The entry point of the program.
if __name__ == '__main__':
    main()
