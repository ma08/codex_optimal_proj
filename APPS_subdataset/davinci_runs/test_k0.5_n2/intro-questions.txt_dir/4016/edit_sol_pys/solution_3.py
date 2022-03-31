

# SOLUTION
# This is a really interesting problem. The idea is to find the smallest repeating unit of the string s. This can be done by finding the smallest length of a prefix of t that is a suffix of t as well. Then, we just need to repeat this prefix k times.

# The function to find the smallest repeating unit of s.
# This function is O(n^2) in the worst case.
def findSmallestRepeatingUnit(s):
    n = len(s)
    for i in range(n//2, 0, -1):
        if s[:i] == s[n-i:]:
            return s[:i]
    return s

# The main function that prints the result.
def main():
    n, k = map(int, input().split())
    s = input()
    print(findSmallestRepeatingUnit(s) * k)

# The entry point of the program.
if __name__ == '__main__':
    main()
