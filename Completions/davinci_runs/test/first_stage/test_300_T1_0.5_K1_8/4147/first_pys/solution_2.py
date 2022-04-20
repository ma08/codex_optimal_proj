

N, A, B, C = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

li.sort()

d = {}
for i in range(len(li)):
    if li[i] in d:
        d[li[i]].append(i)
    else:
        d[li[i]] = [i]

def get_key(d, val):
    for key, value in d.items():
        if val in value:
            return key
    return "key doesn't exist"

def get_val(d, key):
    for k, v in d.items():
        if k == key:
            return v
    return "key doesn't exist"

ans = 10**10
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or k == i:
                continue
            if li[i] + li[j] + li[k] == A + B + C:
                if li[i] == A:
                    if li[j] == B:
                        if li[k] == C:
                            ans = min(ans, 0)
                        else:
                            ans = min(ans, abs(C - li[k]))
                    else:
                        if li[k] == C:
                            ans = min(ans, abs(B - li[j]))
                        else:
                            ans = min(ans, abs(B - li[j]) + abs(C - li[k]))
                else:
                    if li[j] == B:
                        if li[k] == C:
                            ans = min(ans, abs(A - li[i]))
                        else:
                            ans = min(ans, abs(A - li[i]) + abs(C - li[k]))
                    else:
                        if li[k] == C:
                            ans = min(ans, abs(A - li[i]) + abs(B - li[j]))
                        else:
                            ans = min(ans, abs(A - li[i]) + abs(B - li[j]) + abs(C - li[k]))
            elif li[i] + li[j] == A + B:
                if li[i] == A:
                    ans = min(ans, abs(B - li[j]) + abs(C - (li[i] + li[j])))
                else:
                    ans = min(ans, abs(A - li[i]) + abs(B - li[j]) + abs(C - (li[i] + li[j])))
            elif li[i] + li[j] == A + C:
                if li[i] == A:
                    ans = min(ans, abs(C - li[j]) + abs(B - (li[i] + li[j])))
                else:
                    ans = min(ans, abs(A - li[i]) + abs(C - li[j]) + abs(B - (li[i] + li[j])))
            elif li[i] + li[j] == B + C:
                if li[i] == B:
                    ans = min(ans, abs(C - li[j]) + abs(A - (li[i] + li[j])))
                else:
                    ans = min(ans, abs(B - li[i]) + abs(C - li[j]) + abs(A - (li[i] + li[j])))
            elif li[i] + li[j] + li[k] == A + B:
                if li[i] == A:
                    ans = min(ans, abs(B - li[j]) + abs(C - li[k]))
                else:
                    ans = min(ans, abs(A - li[i]) + abs(B - li[j]) + abs(C - li[k]))
            elif li[i] + li[j] + li[k] == A + C:
                if li[i] == A:
                    ans = min(ans, abs(C - li[j]) + abs(B - li[k]))
                else:
                    ans = min(ans, abs(A - li[i]) + abs(C - li[j]) + abs(B - li[k]))
            elif li[i] + li[j] + li[k] == B + C:
                if li[i] == B:
                    ans = min(ans, abs(C - li[j]) + abs(A - li[k]))
                else:
                    ans = min(ans, abs(B - li[i]) + abs(C - li[j]) + abs(A - li[k]))
print(ans)