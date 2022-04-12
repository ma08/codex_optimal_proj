

n, m = map(int, input().split())

if n > m:
    print("Dr. Chaz needs", n-m, "more piece[s] of chicken!") #print the difference of n and m with the word "more"
else:
    print("Dr. Chaz will have", m-n, "piece[s] of chicken left over!") #print the difference of m and n
