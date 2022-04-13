# #

# N = int(input())
# costumes = []
# for i in range(N):
#     costumes.append(input())

# costume_freq = {}
# for costume in costumes:
#     if costume in costume_freq:
#         costume_freq[costume] += 1
#     else:
#         costume_freq[costume] = 1

# max_freq = max(costume_freq.values())
# for costume in sorted(costume_freq):
#     if costume_freq[costume] == max_freq:
#         print(costume)

N = int(input())

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(N):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
