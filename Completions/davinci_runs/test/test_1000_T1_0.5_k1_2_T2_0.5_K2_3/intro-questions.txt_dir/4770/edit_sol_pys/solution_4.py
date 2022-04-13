

#The following is the solution to the problem: https://open.kattis.com/problems/chicken

n, m = map(int, input().split())

if (n < m):
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(m-n))
elif (n > m):
else:
    print("Dr. Chaz will have 0 piece[s] of chicken left over!")
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(n-m))
