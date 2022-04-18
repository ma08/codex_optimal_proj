# input
a, b = map(int, input().split())


# calc
if a + b >= 10:
    ans = "error"
else:
    ans = a + b

# output
print(ans)
