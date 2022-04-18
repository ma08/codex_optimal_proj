

# SOLUTION
# For each letter, find the largest substring that contains that letter and is K-beautiful
# The answer is the max of these lengths.
# Time: O(N^2)
# Space: O(N)

def get_beautiful_substring(s, k):
    ans = 0
    for letter in set(s):
        for i in range(len(s)):
            if s[i] == letter:
                j = i
                while j < len(s) and s[j] == letter:
                    j += 1
                j -= 1
                if (j-i+1) % k == 0:
                    ans = max(ans, j-i+1)
    return ans

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    print(get_beautiful_substring(s, k))
