
#The following is the solution to the problem: https://open.kattis.com/problems/chicken

n, m = map(int, input().split())

if (n < m):
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(m-n))
elif (n > m):
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(n-m))
