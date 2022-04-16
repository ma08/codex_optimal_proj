

def find_max_pow(x):
    for i in range(2, x+1):
        for j in range(2, x+1):
            if i**j <= x:
                ans = i**j
            else:
                break
    return ans

print(find_max_pow(int(input())))
