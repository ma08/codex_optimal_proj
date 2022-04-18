import random

# 1.


K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')
else:

# 2.

N = int(input())
a = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans += a[i] * a[j]

print(ans)

# 3.

N = int(input())
a = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            ans += a[i] * a[j] * a[k]

print(ans)

# 4.

N = int(input())
a = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                ans += a[i] * a[j] * a[k] * a[l]

print(ans)

# 5.

N = int(input())
a = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                for m in range(N):
                    ans += a[i] * a[j] * a[k] * a[l] * a[m]

print(ans)

# 6.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] == S[j]:
            ans += 1

print(ans)

# 7.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if S[i] == S[j] and S[j] == S[k]:
                ans += 1

print(ans)

# 8.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                if S[i] == S[j] and S[j] == S[k] and S[k] == S[l]:
                    ans += 1

print(ans)

# 9.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    if S[i] == S[j] and S[j] == S[k] and S[k] == S[l] and S[l] == S[m]:
                        ans += 1

print(ans)

# 10.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    for n in range(m + 1, N):
                        if S[i] == S[j] and S[j] == S[k] and S[k] == S[l] and S[l] == S[m] and S[m] == S[n]:
                            ans += 1

print(ans)

# 11.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    for n in range(m + 1, N):
                        for o in range(n + 1, N):
                            if S[i] == S[j] and S[j] == S[k] and S[k] == S[l] and S[l] == S[m] and S[m] == S[n] and S[n] == S[o]:
                                ans += 1

print(ans)

# 12.

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    for n in range(m + 1, N):
                        for o in range(n + 1, N):
                            for p in range(o + 1, N):
                                if S[i] == S[j] and S[j] == S[k] and S[k] == S[l] and S[l] == S[m] and S[m] == S[n] and S[n] == S[o] and S[o] == S[p]:
                                    ans += 1

print(ans)

# 13.

N = int(input())
x = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if i < j:
            ans += x[i] * x[j]

print(ans)

# 14.

N = int(input())
x = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i < j < k:
                ans += x[i] * x[j] * x[k]

print(ans)

# 15.

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if i < j < k < l:
                    ans += A[i] * A[j] * A[k] * A[l]

print(ans)

# 16.

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                for m in range(N):
                    if i < j < k < l < m:
                        ans += A[i] * A[j] * A[k] * A[l] * A[m]

print(ans)

# 17.

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):

    print(S)
