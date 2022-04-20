

N = int(input())
S = input()

def get_num_slimes(N, S):
    count = 1
    for i in range(1, N):
        if S[i] != S[i - 1]:
            count += 1
    return count

print(get_num_slimes(N, S))