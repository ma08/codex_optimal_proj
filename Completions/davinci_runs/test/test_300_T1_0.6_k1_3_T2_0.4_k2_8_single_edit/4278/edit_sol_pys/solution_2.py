'''
https://www.hackerrank.com/challenges/pairs
'''


N, K = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if abs(nums[i] - nums[j]) == K:
            count += 1

print(count)

'''
https://www.hackerrank.com/challenges/sherlock-and-anagrams
'''

T = int(input())
for i in range(T):
    S = input()
    N = len(S)

count = 0

    for i in range(N):
        for j in range(i+1, N+1):
            word_i = S[i:j]
            word_j = word_i[::-1]
            for k in range(i+1, N):
                for l in range(k+1, N+1):
                    word_k = S[k:l]
                    word_l = word_k[::-1]
                    if sorted(word_i) == sorted(word_k):
                        count += 1

print(count)
